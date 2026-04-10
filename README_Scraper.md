# Semantic Scholar API Scraper

A Python tool to search and scrape academic papers from the Semantic Scholar API. The scraper searches for papers based on a query string and year range, then exports the results to a CSV file.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or download this repository

2. Install the required dependencies:

Install modules with:
```bash
pip install -r requirements.txt
```

## Configuration

### Setting up the `.env` file

The scraper uses an optional API key from Semantic Scholar. While the API works without a key, using one provides higher rate limits.

1. **Create a `.env` file** in the project root directory (same folder as `semscholarscraper.py`)

2. **Get your API key** (optional but recommended):
   - Visit: https://www.semanticscholar.org/product/api#api-key-form
   - Request an API key
   - Copy the key you receive

3. **Add the API key to your `.env` file**:

```env
SEMANTIC_SCHOLAR_API_KEY=your_api_key_here
```

**Example `.env` file:**
```env
SEMANTIC_SCHOLAR_API_KEY=abc123xyz789yourkeyhere
```

**Important Notes:**
- The `.env` file is already in `.gitignore`, so it won't be committed to version control
- Never share your API key publicly
- If you don't have an API key, you can leave the `.env` file empty or omit it entirely - the scraper will work with shared rate limits

### Alternative: Environment Variables

Instead of using a `.env` file, you can also set the environment variable directly:

**On macOS/Linux:**
```bash
export SEMANTIC_SCHOLAR_API_KEY="your_api_key_here"
```

**On Windows (Command Prompt):**
```cmd
set SEMANTIC_SCHOLAR_API_KEY=your_api_key_here
```

**On Windows (PowerShell):**
```powershell
$env:SEMANTIC_SCHOLAR_API_KEY="your_api_key_here"
```

## Usage

1. **Make sure your `.env` file is set up** (if using an API key)

2. **Run the scraper:**
```bash
python semscholarscraper.py
```

3. **Follow the interactive prompts:**
   - Enter your search query (e.g., "machine learning", "quantum computing")
   - Choose whether to use the default year range (1989-2026) or specify a custom range
   - Wait for the API requests to complete

4. **Find your results:**
   - The results will be saved to `semscholar_results_api.csv` in the same directory
   - The CSV file includes columns: Nr., Authors, Year, Title, Venue, Abstract, Link, DOI

## Example

```bash
$ python semscholarscraper.py
Semantic Scholar API Scraper
Dieses Skript nutzt die offizielle Academic Graph API und speichert die Ergebnisse als CSV.

Bitte gib deinen Suchstring ein:
neural networks
Soll der Default-Suchzeitraum (1989-2026) verwendet werden?
[j/n]: n
Bitte gib den Suchzeitraum im Format XXXX-XXXX ein, z.B. 1994-2024:
2020-2024

Suche nach: 'neural networks' im Zeitraum 2020-2024
Bitte warte, die API-Anfragen laufen...
...
Insgesamt erhaltene Paper: 1000
CSV erfolgreich geschrieben: semscholar_results_api.csv
```

## License

MIT License - see LICENSE file for details
