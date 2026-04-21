import sys
import os
import json
from firecrawl import FirecrawlApp

# Automatically add the parent directory to sys.path so we can import API.keys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

from API.keys import FIRECRAWL_API_KEY

app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# Crawl the full site — limit to 30 pages to get broad coverage
result = app.crawl_url(
    "https://ikes.com/",
    params={
        "limit": 30,
        "scrapeOptions": {
            "formats": ["markdown"]
        }
    }
)

# Save the JSON file right next to this script in the Competitors folder
output_path = os.path.join(SCRIPT_DIR, "UNCLE-IKES-RAW-SCRAPE.json")
with open(output_path, "w") as f:
    json.dump(result if isinstance(result, dict) else result.model_dump(), f, indent=2)

print(f"Crawl complete.")
if isinstance(result, dict):
    pages = result.get("data", [])
else:
    pages = result.data if hasattr(result, "data") else []

print(f"Pages crawled: {len(pages)}")
for page in pages:
    if isinstance(page, dict):
        print(f"  - {page.get('metadata', {}).get('url', 'unknown')}")
    else:
        print(f"  - {page.metadata.url if hasattr(page, 'metadata') else 'unknown'}")
