import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# Felder, die von SemScholar gezogen werden.
FIELDS = ",".join([
    "title",
    "year",
    "venue",
    "abstract",
    "url",
    "authors",
    "externalIds"
])


# Maximale Anzahl Ergebnisse pro Chunk (GET-API ist auf offset+limit <= 1000 begrenzt)
MAX_RESULTS_PER_CHUNK = 1000
PAGE_SIZE = 100  # <= 100 laut Doku
# SemScholar shared-limit: 1 request/sec -> kleine Sicherheitsspanne
MIN_DELAY_SECONDS = 1.05
# Größe der Jahr-Teilintervalle (klein halten, um unter 1000 pro Chunk zu bleiben)
CHUNK_YEARS = 5


def get_api_headers():
    """
    Liest optional einen API-Key aus der Umgebungsvariable SEMANTIC_SCHOLAR_API_KEY.
    Wenn keiner gesetzt ist, wird die API ohne Key genutzt (hat dann Shared-Limit).
    Key kann hier angefordert werden: https://www.semanticscholar.org/product/api#api-key-form
    Einrichtung über Terminal: setx SEMANTIC_SCHOLAR_API_KEY "Zeichenfolge"
    """
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key
    return headers


def parse_year_range(year_range: str) -> tuple[int, int]:
    start, end = year_range.split("-")
    return int(start), int(end)


def chunk_year_ranges(year_range: str, chunk_size: int = CHUNK_YEARS) -> list[str]:
    start, end = parse_year_range(year_range)
    ranges = []
    current = start
    while current <= end:
        chunk_end = min(current + chunk_size - 1, end)
        ranges.append(f"{current}-{chunk_end}")
        current = chunk_end + 1
    return ranges


def search_chunk(query: str, year_range: str, headers: dict) -> list[dict]:
    """
    GET-Suche für einen Jahr-Chunk; respektiert 1000er Limit der API.
    """
    all_papers: list[dict] = []
    offset = 0
    last_request = 0.0
    backoff = MIN_DELAY_SECONDS

    while offset < MAX_RESULTS_PER_CHUNK:
        limit = min(PAGE_SIZE, MAX_RESULTS_PER_CHUNK - offset)

        params = {
            "query": query,
            "year": year_range,
            "limit": limit,
            "offset": offset,
            "fields": FIELDS,
        }

        elapsed = time.perf_counter() - last_request
        if elapsed < MIN_DELAY_SECONDS:
            time.sleep(MIN_DELAY_SECONDS - elapsed)

        print(f"Request: year_range={year_range}, offset={offset}, limit={limit}")
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=30)
        last_request = time.perf_counter()

        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            try:
                retry_after = float(retry_after) if retry_after else backoff
            except ValueError:
                retry_after = backoff

            wait_time = max(MIN_DELAY_SECONDS, retry_after, backoff)
            print(f"  -> 429 Too Many Requests, warte {wait_time:.1f}s und versuche erneut...")
            time.sleep(wait_time)
            backoff = min(backoff * 2, 60)
            continue

        backoff = MIN_DELAY_SECONDS

        if response.status_code != 200:
            print(f"Request failed with status {response.status_code}: {response.text}")
            break

        data = response.json()
        papers = data.get("data", [])
        total = data.get("total")
        next_offset = data.get("next")

        print(f"  -> erhalten: {len(papers)} Einträge (total={total}, next={next_offset})")

        if not papers:
            break

        all_papers.extend(papers)

        if next_offset is None:
            break
        offset = next_offset

    return all_papers


def search_papers(query: str, year_range: str) -> list[dict]:
    """
    Ruft die API chunkweise (Jahr-Teilintervalle) auf, um das 1000er Limit pro GET-Search zu umgehen.
    """
    headers = get_api_headers()
    all_papers: list[dict] = []

    year_chunks = chunk_year_ranges(year_range, CHUNK_YEARS)
    print(f"Suche wird in {len(year_chunks)} Teil-Intervalle aufgeteilt: {', '.join(year_chunks)}")

    for yr in year_chunks:
        chunk_papers = search_chunk(query, yr, headers)
        all_papers.extend(chunk_papers)

    return all_papers


def flatten_papers_to_rows(papers: list[dict], query: str, year_range: str) -> list[dict]:
    rows: list[dict] = []

    for p in papers:
        authors = p.get("authors", []) or []
        author_names = ", ".join(a.get("name", "") for a in authors if a.get("name"))

        external_ids = p.get("externalIds", {}) or {}
        doi = external_ids.get("DOI")

        abstract = p.get("abstract")
        if abstract:
            abstract = abstract.replace("\n", " ").replace("\r", " ")

        row = {
            "Query": query,
            "YearRange": year_range,
            "Authors": author_names,
            "Year": p.get("year"),
            "Title": p.get("title"),
            "Venue": p.get("venue"),
            "Abstract": abstract,
            "Link": p.get("url"),
            "DOI": doi
        }
        rows.append(row)

    return rows


def main():
    print("Semantic Scholar API Scraper")
    print("Dieses Skript nutzt die offizielle Academic Graph API und speichert die Ergebnisse als CSV.\n")

    search = input("Bitte gib deinen Suchstring ein:\n")

    # Festlegung des Default-Suchzeitraums:
    year_range = "1989-2026"
    if input(f"Soll der Default-Suchzeitraum ({year_range}) verwendet werden?\n[j/n]: ").lower() != "j":
        year_range = input("Bitte gib den Suchzeitraum im Format XXXX-XXXX ein, z.B. 1994-2024:\n")

    print(f"\nSuche nach: '{search}' im Zeitraum {year_range}")
    print("Bitte warte, die API-Anfragen laufen...")

    papers = search_papers(query=search, year_range=year_range)

    print(f"\nInsgesamt erhaltene Paper: {len(papers)}")

    if not papers:
        print("Keine Ergebnisse – eventuell Suchbegriff/Zeitraum anpassen.")
        return

    rows = flatten_papers_to_rows(papers, search, year_range)

    df = pd.DataFrame(rows)
    df.index = df.index + 1  # Index ab 1, wie in deinem alten Skript

    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{timestamp}_semscholar_results_api.csv")
    df.to_csv(output_file, index_label="Nr.")

    print(f"CSV erfolgreich geschrieben: {output_file}")


if __name__ == "__main__":
    main()
