import os
from firecrawl import FirecrawlApp
import json

app = FirecrawlApp(api_key="fc-04ddfaee35a14d38a7b7b020288f4e07")

try:
    scrape_result = app.scrape_url('https://borednbuzzed.com/', params={'formats': ['extract'], 'extract': {'prompt': 'Extract a list of all high quality image URLs from the page, especially lifestyle photos, product photos, and the Jim Jones event.'}})
    print(json.dumps(scrape_result, indent=2))
except Exception as e:
    print(f"Error: {e}")
