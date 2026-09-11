# Royal Flush

A silly front-facing 3D tapping game. Survive a 20-second sitting while the bathroom falls apart.

## Play locally

Open `index.html` in a modern browser with WebGL enabled. An internet connection is needed for the pinned Three.js library and the display helpers. No installation or build is needed to play the included version.

If your browser restricts local-file scripts, run `python -m http.server 8000 --bind 127.0.0.1` from this folder and open http://localhost:8000.

Choose a difficulty, click **Take a seat**, then tap the main button or press and release Space while it is focused. Holding Space does not generate repeated taps. Music starts with the round. **Sound on/off** controls music and effects together.

## Put it on GitHub Pages

1. Unzip the package and create a GitHub repository named `royal-flush`.
2. Upload the contents of this folder to the repository. `index.html` must be at the repository root, not inside another `royal-flush` folder. Upload the files, not the ZIP itself.
3. Open **Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**.
4. Select your branch (usually `main`) and **/(root)**, then save.
5. When deployment finishes, use the link shown in Pages settings. It will normally be `https://YOUR-USERNAME.github.io/royal-flush/`.

The prebuilt `index.html` contains the game and its music, so publishing does not require Python, npm, a backend, API keys, or a custom workflow. The `.nojekyll` file is included for static hosting. If a browser upload omits hidden files, the HTML still works with the default Pages build.

Official setup instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Included features

- 20-second rounds; 50, 90, or 140 taps for the three difficulty levels.
- Cartoon 3D character with wild eyes, a reddening face, and nose/ear steam.
- Cupboard, sink, mirror, vanity, and toilet-roll holder.
- Water starts at 20% progress, the roll falls at 42%, and wall tiles start falling at 60%.
- Paper spills across the floor, water forms a puddle, and the bathroom resets on replay.
- Comic synthesized trumping and wind, plus the opening 20 seconds of the supplied Gummy Jump Fever track.
- A large final PLOP, sound effect, animated score tally, and session best score.

## Edit and rebuild

The editable source is `src/game.html`. It contains the markup, styles, and JavaScript together. `src/page-template.html` supplies the standalone page wrapper and display styles. Music is in `assets/gummy-jump-fever-round.mp3`.

After editing, run:

```sh
python scripts/build.py
```

Commit the rebuilt `index.html` along with your source changes. Pages serves the committed HTML; it does not automatically run the Python build script.

Key settings in `src/game.html`:

- `ROUND_SECONDS`: round length (currently 20). Also update the visible time labels if changing it, and provide a long enough music clip.
- Difficulty `<option>` values: tap targets.
- `bathroom()`: water, paper, and tile triggers.
- `finish()`: points and rank calculation.
- `musicGain.gain.value`: music level relative to effects.

Score = taps × 10, plus 100 for the water event, 150 for the roll event, 20 per fallen tile, and 500 for reaching the tap target. Scores are per-session and disappear on reload. This prototype has no online leaderboard or multiplayer.

## Dependencies and media

Three.js 0.160.1 is imported from jsDelivr. The exported display wrapper uses Floating UI 1.7.3/1.7.4 from unpkg. These dependencies require network access. Audio is embedded at build time and does not call a music service.

The music asset is the supplied Gummy_Jump_Fever.mp3, trimmed to approximately 20 seconds. No license for that track is granted by this package. No open-source license has been selected for the project.

## Validation

The export, rebuild, JavaScript syntax, and ZIP contents were checked during packaging. Browser gameplay and sound playback have not been re-tested in the exported version.
