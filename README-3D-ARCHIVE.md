# Royal Flush

A three-level 3D tapping game with an increasingly distressed cast and destructible bathrooms.

## Play

Open `index.html` in a modern browser with WebGL enabled. Internet access is needed for the pinned Three.js library. Music is embedded; no backend, npm installation, or API key is required.

If your browser restricts local files, run `python -m http.server 8000 --bind 127.0.0.1` in this folder, then open http://localhost:8000.

Choose an unlocked level and press START. Tap FLUSH, or press and release Space while it is focused. Holding a key does not produce repeated taps.

## Levels

| Level | Character | Predicament | Target | Music |
| --- | --- | --- | --- | --- |
| 1 | Banana Bandit | Too many bananas | 110 taps | Gummy Jump Fever |
| 2 | Protein Powerhouse | Too much protein, in a gym toilet | 135 taps | Final Set Hero |
| 3 | The Throne King | A kingdom of cheese | 160 taps | Lift on the Throne |

Attempts last **up to 35 seconds**. Reaching 100% ends the attempt immediately. The next level requires **3,000 points in one attempt**, with no carry-over. The meter starts generously and requires progressively more taps per percentage point near the end. Later levels require more total taps.

Scoring:

- Complete a level: 3,000 points.
- Speed bonus: 100 points per second remaining, rounded down to whole points.
- Golden Toilet Brush, Bleach of Glory and Emergency Laxative remain non-scoring achievements.
- Failed attempts earn proportional progress points below 3,000 and show the exact shortfall.

NEXT advances; RETRY starts a fresh attempt. Only successful attempts enter the campaign total. Complete all three levels in one run for the Royal Relief Meter finale. Unlocks are saved in browser storage when available; campaign scores last for the current run.

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

## Speed scoring and campaign finale

A successful attempt earns 3,000 completion points plus 100 points per second remaining, rounded down to whole points. Time is frozen at completion. Incomplete attempts earn progress points below 3,000 and cannot unlock the next level. Humour awards remain visual achievements and add no fixed bonus. Round lengths and tap targets are unchanged.

Only successful attempts contribute to the current campaign; retries do not accumulate points. Starting from the menu starts a fresh run. Level shortcuts remain available as practice; complete Levels 1, 2 and 3 in one run to see the grand finale. NEW RUN resets all campaign scores and begins Level 1.

After the last level result, the Royal Relief Meter adds the three level scores in separate animated bursts with matching tally audio. Its reservoir and needle use a fixed 0–19,500 scale. Final ranks are Respectable Relief below 12,000, Plumbing Menace at 12,000, Royal Flush at 15,000, and Porcelain Legend at 18,000. The final score is the exact sum of the successful level scores.

Finale verification: controlled finishes with 4, 12 and 20 seconds remaining scored 3,400, 4,200 and 5,000, totaling 12,600. Browser checks passed for failed-attempt exclusion, sequential count-up, automatic finale, New Run reset, and desktop/mobile layouts.

## Polish pass: timing, comfort and replay

- Three Perfect Flush opportunities unlock at 20%, 45% and 70% relief. Pause during the one-second amber charge, then tap within the 650 ms green window after at least 650 ms without tapping. A successful timing tap adds eight extra relief units. Continuous tapping and automatic hold taps cannot collect it. Missing the opportunity does not remove progress.
- The flush button has a mechanical click, press travel and independent green/amber glow; relief responds with a small pulse. Important effects temporarily lower the music.
- OPTIONS offers separate music/effects levels, reduced motion, and Gentle Play. Options are available between rounds. Gentle Play holds FLUSH or Space at 4.8 relief units per second; releasing allows a manually timed Perfect Flush. Classic and Gentle Play store separate per-level and campaign personal bests. Mode is fixed for each run.
- Personal bests and preferences persist locally when browser storage is available. Failed attempts report the exact remaining taps alongside their point shortfall. Results separate completion points, speed points and the mode-specific level best; the finale shows the campaign best.
- Level 1 has a smoother shaped shirt, swept hair, seams, badge, hand details, softer lighting/shadows, body/face anticipation and a relief pose. The mouse's escape direction varies between attempts; lower message placement leaves more of the scene visible. Reduced motion suppresses the added camera movement and relief pulse.

Browser checks covered actual pointer holding, timing success, rapid-tap rejection, preference controls, separate mode records, round resets, campaign totals, finale transition and desktop/mobile layouts. Artwork remains procedural 3D, with Level 1 serving as the visual benchmark for future character-model work.

## Challenge menu and ready countdown

The home screen retains the 3D toilet/whirlpool and adds rounded challenge cards with portraits, setting names, one-to-three difficulty stars, selection borders and locked states. Cards stack on narrow screens. Level 1 starts the full campaign; unlocked later levels are clearly labelled practice. Rounded panels and consistent colours carry through the HUD, results and final meter.

START FLUSH, retries, next levels and new campaigns reveal the scene and run a 3–2–1 countdown. Taps are disabled and the level soundtrack is stopped during the countdown. At FLUSH, gameplay music, input and the full 35-second timer begin together. Perfect Flush is taught in play through HOLD OFF / FLUSH NOW messages and WAIT / NOW labels on the flush button, so colour is not the only cue. The confusing TAP GREEN home-screen message is removed.

Browser checks passed for challenge locks, desktop/mobile layout, countdown input and music gating, full round time, next-level countdown, Perfect Flush labels and practice messaging.
