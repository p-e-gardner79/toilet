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
| 2 | Protein Powerhouse | Too much protein, in a gym toilet | 105 taps | Final Set Hero |
| 3 | The Throne King | A kingdom of cheese | 125 taps | Lift on the Throne |

Attempts last **up to 35 seconds**. Reaching 100% ends the attempt immediately. The next level requires **3,000 points in one attempt**, with no carry-over. The meter starts generously and requires progressively more taps per percentage point near the end. Later levels require more total taps.

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

The inline preview uses compressed full-length menu music and 35-second gameplay clips. The export uses MP3 versions. The user supplied the tracks; this package grants no music license. No project open-source license has been selected.

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

## Event sound effects

User-supplied steam train, sink burst, four random tile crashes, and final splash effects are embedded in the game. Steam and water trigger once per attempt. Tile sounds avoid immediate repeats and limit overlapping crashes. Finishing clears other effects before the splash; retry and menu transitions clear all effects. The SOUND control mutes music and effects together. Original MP3 files and compressed preview versions are in assets; effects-manifest.json records the supplied filenames.

Headless Edge verified all seven effects decode to non-silent audio, steam/water do not retrigger every frame, tile selection varies, the final splash replaces active effects, and retries clear effects.

## Level 1 bathroom panic

All rounds have a 35-second limit, with targets of 110, 135 and 160 taps. Reaching 100% still completes the round immediately; each attempt must earn at least 3,000 points to unlock the next level. Music clips cover the full time limit.

Level 1 adds rattling cupboard doors, a panicked mouse carrying a tiny toilet roll, a leap and escape with dust, progressive branching floor cracks and a falling KEEP CALM sign. The mouse appears after tiles start falling and its escape continues through an early finish. Replays reset all props; the new sequence is exclusive to Level 1. A brief pause precedes the final splash.

Browser checks covered the tile-before-mouse sequence, opening doors, complete escape, growing cracks, falling sign, next-level reset and 35-second decoded music durations.

## Menu activation and toilet roll sounds

Audio initialization now begins before scene loading, preserving clicks and key presses during loading. Every menu entry requests playback, and focus or visibility restoration retries it. ENABLE SOUND is shown only while the audio context is not running. Browsers that prohibit audible autoplay still require a user interaction; the game cannot override that policy.

The supplied holder effect plays once at detachment. The paper effect plays once when the roll reaches the floor. Both use the shared sound control and are cleared on finish, retry or menu return. Browser checks verified decoded non-silent clips, separate event timing, no frame-by-frame retrigger, audio-context reuse, menu restart, and automatic menu playback in the standalone file.

## Level 2: The Final Rep

Level 2 now uses a separate gym with a lifting platform, squat rack, mirrors, treadmill, weights and three reacting gym members. The bulky protagonist has a smaller bald head, moustache, sweatband, BULK MODE vest, lifting belt, wrist wraps and skinny calves. His MASS REGRET shaker accompanies the SIX PROTEIN SHAKES / ZERO FIBRE predicament.

The trainer approaches to spot him, loses a clipboard at halfway and flees. A lifter lowers then escapes with a barbell; the treadmill runner accelerates in place. Plates bounce at the final splash and a NEW PERSONAL BEST sign appears before the score tally. The existing Level 2 music and 35-second, 135-tap target remain. Bathroom props and their destruction sounds are hidden/suppressed specifically in Level 2.

LEVEL-2-SOUND-REQUESTS.md contains eight ready-to-use sound generation prompts and optional voice lines. These new recordings are not yet supplied; existing sound effects support the scene in the meantime. Browser checks covered the separate environment, character, event sequence, escaped actors, stationary runner, score, celebration and Level 1 restoration.

### Gym cast refinement

The spotter has swept hair, the lifter a mohawk and the runner a ponytail. All three have broader shoulders and defined arm and leg muscles. The lifter uses articulated upper arms, elbows and forearms with both hands attached to the bar through curls, lowering and escape. The spotter stands further forward and to the right, with the treadmill moved back and outward. Browser checks at a 936-pixel viewport verified visibility, hand-to-bar alignment, evacuation, scoring and Level 1 restoration.

## Supplied gym audio and final collapse

The eight gym recordings are now embedded and connected to rattle, clipboard blast, barbell lowering, fleeing footsteps, carried barbell, treadmill sprint, final plate bounce and hanging sign events. The treadmill loops until the round ends. At the final plop the yellow runner tumbles off the treadmill onto the gym floor, stays down during results, and resets upright for a new attempt.

The supplied tally sound plays on every level for exactly the 2.4-second score animation, looping the two-second source to cover the complete count. It starts at the same level-specific delay as the visual tally and stops at completion; the final splash preserves the scheduled tally. Menu and retry transitions cancel all effects.

Headless Edge verified all 18 effects decode to non-silent audio, gym events trigger, treadmill stops, runner collapses, Level 1/2 tally start offsets and duration match the visuals, and audio/poses reset correctly.

## Level 3: The Royal Blockage

A separate gold-and-burgundy palace replaces the bathroom, with stained glass, a velvet canopy, marble dais, carpet, chandelier, banners, cheese banquet and armour. The king wears a cape, larger crown, curled moustache and pointed beard. A formal butler escalates from prune to remedy to giant brush; the trumpeter reacts, guards flee and one loses his helmet. Armour collapses as pressure rises. The final splash launches the crown, ripples the carpet and reveals THE KING HAS BEEN RELIEVED as the court bows. The crown lands crookedly before the score tally begins at 3.1 seconds. Existing music, 35-second limit, 160-tap target and score rules remain.

LEVEL-3-SOUND-REQUESTS.md supplies twelve palace sound prompts plus optional voice lines; these new recordings are not yet supplied. Browser checks verified Level 3 event progression, scoring, crown landing and returning to Level 1.

### Palace recordings

Six supplied palace effects now play at their matching events: opening fanfare, tray at 10% progress, banner gust at 30%, chandelier at 50%, nervous guards at 68%, and collapsing armour at 82%. Each is triggered once per attempt, routed through the shared sound control, and cleared at finish or reset. Browser verification covered decoding, event triggers, no per-frame repetition, cleanup and Level 1 isolation.
