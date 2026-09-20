"""Build the complete offline retro game. Python 3 standard library only."""
from pathlib import Path
import base64
import json
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--fragment-output',type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
assets={}
def embed(name,path,mime):
    assets[name]='data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode('ascii')
for name in ['bathroom','banana','gym','bodybuilder','palace','king','cast','props','deflated','lifter','runner','trainer','sumo','bathhouse']:
    embed(name,root/'assets/retro'/f'{name}.webp','image/webp')
for name,file in [('menuMusic','victory-on-the-throne-menu.mp3'),('music1','gummy-jump-fever-round.mp3'),('music2','final-set-level-two.mp3'),('music3','lift-level-three.mp3'),('music4','sumo-level.mp3'),('bonusMusic','bonus-level.mp3')]:
    embed(name,root/'assets'/file,'audio/mpeg')
for file in (root/'assets').glob('voice-*.mp3'):
    embed(file.stem,file,'audio/mpeg')
for file in (root/'assets').glob('effect-*.mp3'):
    embed(file.stem.removeprefix('effect-'),file,'audio/mpeg')
css=(root/'src/retro.css').read_text(encoding='utf-8')+'\n'+(root/'src/retro-extra.css').read_text(encoding='utf-8')+'\n'+(root/'src/expansion.css').read_text(encoding='utf-8')
script=(root/'src/retro.js').read_text(encoding='utf-8').replace('__GYM_ANIMATION__',(root/'src/gym-animation.js').read_text(encoding='utf-8')).replace('__EXPANSION__',(root/'src/expansion.js').read_text(encoding='utf-8')).replace('__ASSETS__',json.dumps(assets,separators=(',',':'))).replace('__RECTS__',(root/'assets/retro/rects.json').read_text())
fragment=(root/'src/retro.html').read_text(encoding='utf-8').replace('__CSS__',css).replace('__SCRIPT__',script)
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#07162b"><title>Royal Flush — Retro Arcade</title><style>body{margin:0;padding:16px 12px 30px;background:#030d1b}@media(max-width:540px){body{padding:0 0 15px}}</style></head><body>'+fragment+'</body></html>'
(root/'index.html').write_text(page,encoding='utf-8')
if args.fragment_output:
    if len(fragment.encode())>=1_000_000:
        raise SystemExit('The full game exceeds the inline preview limit. Open index.html in a browser; it includes every track and asset.')
    args.fragment_output.write_text(fragment,encoding='utf-8')
print(f'Built full offline retro game: {len(page.encode()):,} bytes, {len(assets)} embedded assets.')

