# Royal Flush

A three-level 3D tapping game with an increasingly distressed cast and destructible bathrooms.

## Play

Open `index.html` in a modern browser with WebGL enabled. Internet access is needed for the pinned Three.js library. Music is embedded; no backend, npm installation, or API key is required.

If your browser restricts local files, run `python -m http.server 8000 --bind 127.0.0.1` in this folder, then open http://localhost:8000.

Choose an unlocked level and press START. Tap FLUSH, or press and release Space while it is focused. Holding a key does not produce repeated taps.

## Levels

| Level | Character | Predicament | Target | Music |
| --- | --- | --- | --- | --- |
| 1 | Banana Bandit | Too many bananas | 85 taps | Gummy Jump Fever |
| 2 | Protein Powerhouse | Too much protein, in a gym toilet | 105 taps | Gummy Jump Fever |
| 3 | The Throne King | A kingdom of cheese | 125 taps | Lift on the Throne |

Attempts last **up to 25 seconds**. Reaching 100% ends the attempt immediately. The next level requires **3,000 points in one attempt**, with no carry-over. The meter starts generously and requires progressively more taps per percentage point near the end. Later levels require more total taps.

Scoring:

- Effort: up to 2,000 points, proportional to progress.
- 25%: Golden Toilet Brush, +200.
- 50%: Bleach of Glory, +300.
- 75%: Emergency Laxative, +500.
- 100%: successful relief, +500.

A completed attempt earns **3,500 points**. Failed attempts show the exact points shortfall. NEXT advances; RETRY resets attempt points and awards. Unlocks are saved in browser storage when available; restricted contexts may retain progress only for the session.

## Audio

The complete Victory on the Throne track plays on the menu, looping only after the full song. The game attempts autoplay on load. Browsers may block audible autoplay until an interaction; the first click or key press anywhere resumes audio. No separate MENU MUSIC press is needed. SOUND/MUTED controls all audio.

The export is a top-level browser page, avoiding the previous iframe's audio-permission boundary. Starting a round stops menu music and starts the level track. Finishing stops gameplay music for the plop.

The inline preview uses compressed full-length menu music and 25-second gameplay clips. The export uses MP3 versions. The user supplied the tracks; this package grants no music license. No project open-source license has been selected.

## GitHub Pages

1. Create a repository, such as `royal-flush`.
2. Upload this folder's contents, with `index.html` at the repository root. Do not upload only the ZIP.
3. Under **Settings → Pages**, choose **Deploy from a branch**, then `main` and `/(root)`.
4. Use the published address shown by GitHub Pages.

Official guide: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Edit and rebuild

Edit `src/game.html`, then run `python scripts/build.py`. Commit the rebuilt `index.html` alongside source changes. GitHub Pages serves that prebuilt file; no custom workflow is needed.

`src/page-template.html` supplies standalone styles; the build extracts its inner document into a top-level page. Music is in `assets/`. Main settings: `ROUND_SECONDS`, `LEVELS`, `AWARDS`, `progress()`, and `attemptScore()`. `applyCharacter()` changes character and room props; `drawInterface()` renders the mesh interface. The optional `--fragment-output` build argument generates the compressed inline preview.

## Checks

Automated tests covered timing, single-attempt scoring, awards, shortfalls, locks, retries, instant completion at 100%, and all levels. Headless Edge completed three-level progression and rendered the gym character. Its audio context was running after interaction and decoded tracks contained non-silent samples, including Level 3. Physical speaker output was not audited.
