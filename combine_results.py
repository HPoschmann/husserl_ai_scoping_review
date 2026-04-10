"""
Kombiniert alle CSVs in einem "out"-Ordner zu einer Datei und vereinheitlicht Duplikate.
- Duplikat-Erkennung: bevorzugt DOI; sonst Titel+Jahr; sonst Link; andernfalls eigene Zeilen-ID.
- Für zusammengeführte Zeilen werden alle genutzten Suchbegriffe (Query) gesammelt.

Pfadauflösung (robust, auch bei anderem Layout):
1) CLI-Argument --out-dir
2) Umgebungsvariable COMBINE_OUT_DIR
3) "out" neben diesem Skript
4) "out" im aktuellen Arbeitsverzeichnis
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


DEFAULT_OUT_DIR = (Path(__file__).resolve().parent / "out").resolve()


def normalize_str(value: Any) -> str | None:
    if isinstance(value, str):
        trimmed = value.strip()
        return trimmed if trimmed else None
    return None


def build_dedup_key(row: pd.Series, row_id: int) -> str:
    doi = normalize_str(row.get("DOI"))
    if doi:
        return f"doi:{doi.lower()}"

    title = normalize_str(row.get("Title"))
    if title:
        year = row.get("Year")
        year_str = str(int(year)) if pd.notna(year) else ""
        return f"title:{title.lower()}|year:{year_str}"

    link = normalize_str(row.get("Link"))
    if link:
        return f"link:{link.lower()}"

    # Fallback: keine dedupbaren Felder, also individuelle ID
    return f"row:{row_id}"


def unique_join(values: Iterable[Any]) -> str:
    seen: list[str] = []
    for v in values:
        norm = normalize_str(v)
        if norm and norm not in seen:
            seen.append(norm)
    return "; ".join(seen)


def first_nonempty(series: pd.Series) -> Any:
    for v in series:
        if isinstance(v, str):
            if v.strip():
                return v
        else:
            if pd.notna(v):
                return v
    return None


def merge_group(group: pd.DataFrame) -> dict[str, Any]:
    merged = {}
    for col in group.columns:
        if col == "Query":
            merged[col] = unique_join(group[col])
        elif col == "YearRange":
            merged[col] = unique_join(group[col])
        elif col == "__dedup_key":
            continue
        else:
            merged[col] = first_nonempty(group[col])
    return merged


def resolve_out_dir(cli_arg: str | None) -> Path:
    """
    Liefert den zu verwendenden out-Ordner (siehe Prioritäten oben).
    """
    candidates: list[Path] = []

    if cli_arg:
        candidates.append(Path(cli_arg).expanduser().resolve())

    env_dir = os.getenv("COMBINE_OUT_DIR")
    if env_dir:
        candidates.append(Path(env_dir).expanduser().resolve())

    candidates.append(DEFAULT_OUT_DIR)
    candidates.append((Path.cwd() / "out").resolve())

    for cand in candidates:
        if cand.exists():
            return cand
    return candidates[0] if candidates else Path("out")


def combine_csvs(out_dir: Path) -> Path | None:
    if not out_dir.exists():
        print(f"Ordner nicht gefunden: {out_dir}")
        return None

    csv_files = sorted(out_dir.glob("*.csv"))
    if not csv_files:
        print(f"Keine CSV-Dateien in {out_dir}")
        return None

    frames = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            df["SourceFile"] = file.name
            frames.append(df)
            print(f"Eingelesen: {file.name} ({len(df)} Zeilen)")
        except Exception as exc:  # noqa: BLE001
            print(f"Übersprungen (Fehler beim Lesen): {file.name} -> {exc}")

    if not frames:
        print("Keine Dateien erfolgreich eingelesen.")
        return None

    combined = pd.concat(frames, ignore_index=True, sort=False)
    combined["__dedup_key"] = [
        build_dedup_key(row, idx) for idx, row in combined.iterrows()
    ]

    merged_rows = []
    for _, group in combined.groupby("__dedup_key", dropna=False):
        merged_rows.append(merge_group(group))

    result_df = pd.DataFrame(merged_rows)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = out_dir / f"combined_{timestamp}.csv"
    result_df.to_csv(output_file, index=False)
    print(f"Geschrieben: {output_file} ({len(result_df)} Zeilen nach Deduplizierung)")
    return output_file


def main() -> None:
    parser = argparse.ArgumentParser(description="CSV-Ergebnisse zusammenführen und deduplizieren.")
    parser.add_argument(
        "--out-dir",
        help="Pfad zum out-Ordner (optional). Sonst: COMBINE_OUT_DIR oder 'out' neben Skript oder Arbeitsverzeichnis.",
    )
    args = parser.parse_args()

    out_dir = resolve_out_dir(args.out_dir)
    print(f"Nutze out-Ordner: {out_dir}")

    output = combine_csvs(out_dir)
    if output is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
