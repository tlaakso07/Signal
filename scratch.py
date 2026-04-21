import urllib.request
import re
from collections import Counter

url = "https://borednbuzzed.com"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all css links
    css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', html)
    all_colors = []
    
    # Also find inline styles and colors in HTML
    hex_pattern = r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
    inline_hex = re.findall(hex_pattern, html)
    all_colors.extend(inline_hex)

    for link in css_links:
        if link.startswith('//'):
            link = 'https:' + link
        elif link.startswith('/'):
            link = url + link
        try:
            css_req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            css_content = urllib.request.urlopen(css_req).read().decode('utf-8')
            all_colors.extend(re.findall(hex_pattern, css_content))
        except Exception as e:
            pass

    # Process colors
    full_hex = []
    for c in all_colors:
        if len(c) == 3:
            c = c[0]*2 + c[1]*2 + c[2]*2
        full_hex.append(c.lower())
        
    counts = Counter(full_hex)
    print("Top extracted colors:")
    for color, count in counts.most_common(10):
        print(f"#{color.upper()}: found {count} times")
except Exception as e:
    print(e)
