"""Reproduce the normalized-title check for the nine supplementary PhilPapers publications.

The manuscript (Section 4.8) reports that none of the nine publications charted in the external
check appears in the original combined retrieval export or in the title-screening workbook.
This script repeats that check from the repository files.

Run from the repository root:
    python verify_external_title_check.py
Requires openpyxl (pip install openpyxl).

Method: titles are normalized by lower-casing and removing every character that is not a-z or 0-9
(spaces, punctuation, dashes, apostrophes). A publication counts as found if the normalized title
fragment below occurs inside any normalized cell of a row. The fragments are the distinctive main
titles used in the original check; matching a fragment inside a cell is deliberately lenient, so
variant subtitles or truncated titles would still be detected. A publication included in the formal
corpus serves as a positive control and must be found in both files.
"""
import csv
import re
import sys
import warnings
from pathlib import Path

import openpyxl

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
ROOT = Path(__file__).resolve().parent
RAW_EXPORT = ROOT / 'rohdaten_combined_20251205_141147.csv'
TITLE_WORKBOOK = ROOT / 'step1_title_screening_combined.xlsx'

# manuscript reference -> title fragment (full titles in external_PhilPapers_review/external_check_round2.xlsx)
EXTERNAL = {
    '[54] Ferro 2022': 'Meeting the Gaze of the Robot',
    '[55] Brinck & Balkenius 2020': 'Mutual Recognition in Human-Robot Interaction',
    '[56] Poljansek 2025': 'Situation Cognition for Social Robotics',
    '[57] Grueneberg 2026': 'Intentionality and performance',
    '[58] Lopes 2023': 'Can Deep CNNs Avoid Infinite',
    '[59] Lopes 2023': 'Phenomenology as Proto-Computationalism',
    '[60] Mykhailov & Liberati 2023': 'A Study of Technological Intentionality',
    '[61] Wellner 2022': 'Digital Imagination, Fantasy, AI Art',
    '[50] Orbik 2024': 'Husserl’s concept of transcendental consciousness',
}
POSITIVE_CONTROL = {'[38] Weatherby 2022 (formal corpus)': 'Intermittent Legitimacy'}


def norm(value):
    return re.sub(r'[^a-z0-9]', '', str(value).lower())


def raw_rows():
    with RAW_EXPORT.open(encoding='utf-8-sig', newline='') as handle:
        yield from csv.reader(handle)


def workbook_rows():
    book = openpyxl.load_workbook(TITLE_WORKBOOK, read_only=True, data_only=True)
    for sheet in book.worksheets:
        yield from sheet.iter_rows(values_only=True)


def scan(rows, targets):
    wanted = {label: norm(fragment) for label, fragment in targets.items()}
    hits = {label: 0 for label in targets}
    for row in rows:
        cells = [norm(c) for c in row if c is not None and str(c).strip()]
        for label, key in wanted.items():
            if any(key in cell for cell in cells):
                hits[label] += 1
    return hits


def main():
    for path in (RAW_EXPORT, TITLE_WORKBOOK):
        if not path.exists():
            sys.exit(f'missing file: {path.name} (run the script from the repository root)')
    targets = {**EXTERNAL, **POSITIVE_CONTROL}
    results = {RAW_EXPORT.name: scan(raw_rows(), targets), TITLE_WORKBOOK.name: scan(workbook_rows(), targets)}

    ok = True
    for source, hits in results.items():
        print(f'\n{source}')
        for label in targets:
            control = label in POSITIVE_CONTROL
            passed = hits[label] > 0 if control else hits[label] == 0
            ok &= passed
            kind = 'positive control' if control else 'external record'
            print(f'  {"PASS" if passed else "FAIL"}  {label:38s} matching rows: {hits[label]:3d}  ({kind})')
    print('\nResult:', 'none of the nine external publications was found; positive control found.' if ok
          else 'check FAILED - see rows above.')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
