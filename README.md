# Royal Flush — Retro Arcade

The complete four-level game with a plunger bonus, rebuilt in the approved illustrated 1990s arcade style.

## Play

Open `index.html` in a modern browser. Everything is embedded: artwork, all six music tracks, 24 effects and twelve recorded announcer clips. No internet connection, backend, npm installation or API key is required. Tap FLUSH or press Space. On desktop the layout adapts to the window height; phones show the whole scene and large touch controls.

- Level 1: Banana Bandit — 110 relief units, bathroom, Gummy Jump Fever.
- Level 2: The Final Rep — 125 units, gym, Final Set Hero.
- Bonus after Level 2: Plunger Panic — 12 seconds, Bonus-level soundtrack.
- Level 3: Royal Blockage — 140 units, palace, Lift on the Throne.
- Level 4: Sumo Showdown — 150 relief units earned through rhythm, Mount Fuji bathhouse, sumo-level soundtrack.

Each attempt has an expressive recorded arcade announcer calling THREE, TWO, ONE, GO alongside the three-second countdown and up to 35 seconds of play. Reach 100% for 3,000 points plus 100 points per remaining second. Progress becomes harder near the end. Failures stay below 3,000 and show the exact shortfall; attempts never accumulate toward a pass. Awards at 25%, 50% and 75% are cosmetic.

Every main level now uses slow taps, fast taps, a get-ready warning, a sustained held push and a timed release. Release correctly for +12 relief. Gentle play assists only the tapping phases; held pushes and releases remain deliberate. Personal bests are separate for Classic and Gentle.

Complete all four levels in one run for the animated final Royal Relief Meter, per-level breakdown and rank. Starting an unlocked later level is practice and does not fabricate missing campaign scores. Unlocks, options and classic/gentle personal bests use the same storage keys as the previous version when available.

## Animated scenes

- Bathroom: three character expressions, fists/heel movement, steam and sweat, bursting sink, detached toilet roll and unravelling paper, sequential falling tiles, opening cupboard, panicked mouse carrying a tiny roll and escaping, floor cracks and falling KEEP CALM sign.
- Gym: massive moustached bodybuilder, mohawked muscular lifter with animated barbell/hand alignment, green trainer and clipboard, ponytailed yellow runner. Rattling weights, fleeing bystanders, flying clipboard, bouncing plates and the runner falling onto the floor at the final plop.
- Palace: crowned king, butler, trumpeter, two guards and armour. Flying tray, swaying chandelier, escaping guards, falling armour, airborne crown and royal reactions.
- Menu: overhead toilet, animated whirlpool and orbiting crowned turd; illustrated challenge portraits and saved locks.

Animation uses separate sprite layers, expression poses and procedural movement. The original concept pictures are visual references, not static screenshots used as the whole game. See `RETRO-ART.md` for the asset prompt set and provenance.

## Sound and options

The full Victory on the Throne menu recording loops only after its complete duration. Menu playback is attempted automatically; a browser may require the first click/key press before audible playback. Any interaction retries audio, without a separate menu-music button. Level music starts after the countdown. Existing effects accompany their scene events; the tally loop lasts exactly as long as the score count-up (2.4 seconds per round; five 1.6-second stages in the finale, including the bonus).

OPTIONS contains separate music/effects volume, reduced motion, gentle play and optional soft CRT scanlines. The timer and media pause while options are open or the tab is hidden. Music and scene effects were supplied by the user; countdown and coach recordings were also supplied by the user. This package does not grant a separate music license.

## GitHub Pages

Upload the contents of this folder with `index.html` at the repository root. Enable Pages for the desired branch/root folder. The prebuilt page needs no build service. The sibling `royal-flush-github.zip` contains this complete package.

## Edit and build

- `src/retro.html`: interface markup.
- `src/retro.css` and `src/retro-extra.css`: responsive arcade styling.
- `src/retro.js`: game rules, audio and animation.
- `src/expansion.js` and `src/expansion.css`: plunger bonus, sumo rhythm/scene and responsive coach panel.
- `src/gym-animation.js`: pose-driven gym cast and muscle inflation/deflation.
- `assets/retro/`: original PNGs, WebP runtime atlases and sprite rectangles.
- `scripts/build.py`: run with Python 3 to rebuild the offline `index.html`.

The complete game is larger than the conversation's inline-preview limit. Open the standalone page for the full experience. The earlier Level 1 study remains separate. The previous 3D package was preserved as the sibling `royal-flush-3d-archive.zip`; `README-3D-ARCHIVE.md`, `src/game.html` and `scripts/build-3d-archive.py` retain its sources. The current default build produces the retro game.

## Validation

Browser checks cover all levels, locks, input, countdown, exact music selection, Perfect Flush bonuses, scene event ordering, options pause, success/failure, retry reset, score timing and campaign totals. Desktop and phone screenshots were inspected. Additional checks cover gentle play, persisted settings, audio metadata and compact desktop layout. Physical speaker output is not independently measured.


## Gym animation and voiced countdown update

Each new attempt and level has embedded THREE, TWO, ONE, GO voice clips synchronized to the visible countdown. The voice uses the Effects volume and SOUND toggle, pauses with options/tab visibility, and works offline without browser speech services. These now use the supplied ElevenLabs MP3 performance rather than the earlier offline robotic voice. The 35-second timer and tapping still begin only at GO.

The bodybuilder's upper arms, shoulders and chest progressively enlarge with relief progress while the head, feet and toilet stay anchored. At the plop, a short deflation transition reveals a separately illustrated slender character with an oversized vest. The plop lettering moves above him so the reveal remains visible. A retry restores his starting build.

The gym bystanders now use distinct authored poses. The lifter curls through low/middle/high positions with both hands attached to the illustrated bar, sets it on the platform, then runs away. The trainer checks the clipboard, turns to coach, recoils from the blast, loses the separate animated clipboard, and escapes. The runner cycles through stride poses on the moving treadmill belt, speeds up, stumbles off and lands seated on the floor. Reduced-motion mode retains the readable event poses and final reveal while suppressing rapid motion.

New runtime artwork: `assets/retro/deflated.webp`, `lifter.webp`, `runner.webp`, and `trainer.webp`, with original PNG atlases alongside. Current countdown clips are `assets/voice-three.mp3`, `voice-two.mp3`, `voice-one.mp3`, and `voice-go.mp3`. The original combined recording is preserved in `assets/announcer-originals/`; natural pauses were used to split the four words for synchronization. Older WAV files are archived assets and are not embedded or played.

Additional checks cover voice cue ordering on repeated levels, preserved countdown input lock, fixed treadmill contact, changing NPC poses, measurable upper-body growth, full deflation after the plop, collapse and retry reset. The three number clips each fit inside their one-second slots; the GO performance continues naturally into play.

## Plunger and sumo expansion

Campaign order is bathroom → gym → plunger bonus → palace → sumo → final tally. Bonus instructions precede its voiced countdown. Press once as the approaching ring meets the green ring; wait for the plunger to rise before the next beat. A good push earns 100 points, a precise push 150, plus a growing streak bonus capped at 50 per push. Eight good pushes clear the visible blockage and award the Golden Plunger. All twelve seconds remain available to score. Early/late pushes break the streak; repeated taps in the same beat cannot farm points. Even zero points allows the player to continue to Level 3. Bonus points are listed separately in the campaign finale and never contribute to a main-level pass.

At Level 4 the rhythm repeats a 14.6-second cycle: slow taps (4s), fast taps (2.5s), get ready (1.5s), push and hold (5.6s), release (1s). Slow taps need 440ms separation and give 2.6 relief; fast taps need 145ms and give 1.6. During PUSH AND HOLD, keep the mouse/touch button or Space pressed. Pressure builds evenly over the held section, capped at 14 per cycle. Release during the RELEASE window after holding continuously for at least 1.5 seconds to earn +12 relief. Early releases earn no timing bonus; repeated clicks cannot replace the sustained hold. Pausing, losing focus or pointer cancellation safely cancels the hold. Gentle mode still assists tapping phases but the held push and release use the same deliberate controls.

The sumo retains the 35-second deadline and 3,000-point single-attempt clear rule. A test with two slow taps/second, four fast taps/second and correctly held pushes cleared within the 35-second deadline. His expressions intensify, petals drift, pools ripple, birds flee, deck cracks appear and the final plop sends water and a bucket flying. Reduced-motion keeps the cues readable without rapid character shaking.

Existing three-level personal scores and unlocks migrate into four slots. Expanded-campaign records use a separate `expandedCampaign` field so an old three-level total is not compared to the longer run. Your full original sumo and bonus MP3s are embedded without trimming. They begin at GO and stop at the end of their respective round. No network audio service is used.

Validation includes a complete four-level run with earned bonus points, precise/early bonus input, spam protection, pausing, classic sumo clearance, timeout/retry, mobile layouts and the final total including the separate bonus.

## Recorded announcer update

All active speech now comes from the two replacement Arcade (energetic) ElevenLabs takes. The combined countdown is split into THREE/TWO/ONE/GO clips without changing the speaker or speech speed; the displayed countdown remains three seconds and music begins at GO. The original files and a timing manifest are included in `assets/announcer-originals/` and `assets/announcer-manifest.json`.

Slow-down and nice-and-steady alternate on successive sumo cycles. Faster, get ready, push-and-hold, keep-holding and release accompany their actions. Beautiful/what-a-relief plays at each successful main-level plop. Only one announcer clip can play at a time, and music ducks beneath speech. Sound mute, effects volume and game pausing apply to the recordings. No runtime speech service or network connection is needed.

Additional checks verify MP3-only runtime speech, all four countdown beats, playable sustained holds, early-release rejection, click-spam rejection, cancellation on pause, keyboard/mouse releases, bonus-round countdown and phone layout.


## Rhythm from Level 1

All main levels now share the coached controls. See RHYTHM-DIFFICULTY.md for the progression table and METER-SOUND-PROMPTS.md for the requested responsive audio assets. Existing Perfect Flush charge/tap windows have been replaced by held pushes and timed releases across the campaign.


