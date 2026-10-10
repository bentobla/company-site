"""Check all local resources and links on the six Pløtline pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        self.links.extend(v for k, v in attrs if k in ('href', 'src') and v)

pages = [p for locale in ('de', 'en') for p in [Path(locale) / 'projects/plotline.html', *sorted((Path(locale) / 'projects/plotline').glob('*.html'))]]
assert len(pages) == 6
for page in pages:
    parser = Links()
    parser.feed(page.read_text())
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (page.parent / unquote(url.path)).resolve()
        assert target.exists(), f'{page}: broken link {link}'
print(f'All local links/resources on {len(pages)} Pløtline pages exist.')
