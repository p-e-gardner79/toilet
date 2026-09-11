"""Rebuild the deployable index.html using Python 3, with no dependencies."""
from pathlib import Path
from html import escape
import base64

root = Path(__file__).resolve().parents[1]
fragment = (root / 'src/game.html').read_text(encoding='utf-8')
music = base64.b64encode((root / 'assets/gummy-jump-fever-round.mp3').read_bytes()).decode('ascii')
fragment = fragment.replace('__MUSIC_BASE64__', music)
template = (root / 'src/page-template.html').read_text(encoding='utf-8')
assert template.count('__GAME_FRAGMENT__') == 1
document = template.replace('__GAME_FRAGMENT__', escape(fragment))
(root / 'index.html').write_text(document, encoding='utf-8', newline='\n')
print('Built index.html. Ready for GitHub Pages.')
