"""Rebuild the deployable index.html using Python 3, with no dependencies."""
from pathlib import Path
from html import escape
import base64
import argparse
from html.parser import HTMLParser

parser = argparse.ArgumentParser()
parser.add_argument('--fragment-output', type=Path, help='Optionally save the embedded preview fragment')
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
fragment = (root / 'src/game.html').read_text(encoding='utf-8')
music = base64.b64encode((root / 'assets/gummy-jump-fever-round.mp3').read_bytes()).decode('ascii')
if args.fragment_output:
    preview_music = base64.b64encode((root / 'assets/victory-preview-full.opus').read_bytes()).decode('ascii')
    preview_game = base64.b64encode((root / 'assets/gummy-preview.opus').read_bytes()).decode('ascii')
    preview = fragment.replace('__MENU_BASE64__', preview_music).replace('__MUSIC_BASE64__', preview_game)
    preview = preview.replace('__LEVEL3_BASE64__', base64.b64encode((root / 'assets/lift-preview.opus').read_bytes()).decode('ascii'))
    assert len(preview.encode('utf-8')) < 1_000_000, 'Preview exceeds size limit'
    args.fragment_output.write_text(preview, encoding='utf-8', newline='\n')
fragment = fragment.replace('__MUSIC_BASE64__', music)
menu = base64.b64encode((root / 'assets/victory-on-the-throne-menu.mp3').read_bytes()).decode('ascii')
fragment = fragment.replace('__MENU_BASE64__', menu)
fragment = fragment.replace('__LEVEL3_BASE64__', base64.b64encode((root / 'assets/lift-level-three.mp3').read_bytes()).decode('ascii'))
template = (root / 'src/page-template.html').read_text(encoding='utf-8')
assert template.count('__GAME_FRAGMENT__') == 1
document = template.replace('__GAME_FRAGMENT__', escape(fragment))
class FrameExtractor(HTMLParser):
    page = None
    def handle_starttag(self, tag, attrs):
        if tag == 'iframe':
            self.page = dict(attrs).get('srcdoc')
extractor = FrameExtractor()
extractor.feed(document)
assert extractor.page, 'Standalone content is missing'
# Publish as a top-level page, avoiding iframe autoplay delegation restrictions.
document = extractor.page
(root / 'index.html').write_text(document, encoding='utf-8', newline='\n')
print('Built index.html. Ready for GitHub Pages.')
