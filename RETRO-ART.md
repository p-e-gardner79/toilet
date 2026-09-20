# Retro art direction and asset provenance

All new raster artwork was produced with the built-in image generation tool using the approved Level 1 and start-screen concept images as references. The game uses separate illustrated backgrounds, transparent sprite atlases and procedural animation, rather than displaying a static concept screenshot. Soft scanlines are a removable runtime overlay.

Original PNG atlases and compressed WebP runtime versions are in `assets/retro/`. `rects.json` records the alpha-bounded rectangles used by the renderer. The original bathroom/banana PNGs also remain in the separate `royal-flush-retro` animation-study package. Compression and alpha-bound measurement do not alter the artwork's composition.

## Final prompt set

Every prompt requested heavy dark ink outlines, saturated hand-painted 1990s cartoon arcade artwork consistent with the approved reference, and no baked-in UI or scanlines.

- **Bathroom:** clean frontal turquoise tiled bathroom, closed golden cupboard on left, toilet-roll holder, sink and bananas on right, blank poster, rubber duck; central space left empty for the character. No destruction or water is baked in. Generated for the preceding animation study.
- **Banana Bandit:** three transparent full-body poses of the brown-haired adult in purple shirt, seated on his white toilet; calm, strained and wild expressions; identical baseline and scale. Generated for the preceding animation study.
- **Gym:** front-facing gym with red squat rack, mirrored turquoise/purple walls, weight plates and dumbbells, right-side treadmill, lockers, clock, exit sign, hanging THE FINAL REP sign; central 40% empty for the separately animated hero. No characters or toilet.
- **Bodybuilder:** horizontal transparent three-pose atlas; comically massive adult bodybuilder seated on white toilet, black vest, red sweatband/wristbands, bald head, thick moustache, gold belt, blue shorts at ankles, small calves, blue shoes. Calm, strained and wild expressions at consistent scale and baseline.
- **Palace:** frontal throne room with purple canopy curtains, golden columns, turquoise stained glass and marble floor, red carpet, cheese platter, gold toilet brush, shields and armour pedestal. Empty central space and space above for a separate chandelier; no king, throne or toilet.
- **King:** transparent three-pose atlas of a rotund elderly king on a gold-trimmed white toilet, gold jeweled crown, white beard, purple shirt, red ermine cape and gold slippers. Haughty, strained and wild expressions, consistent baseline and proportions.
- **Supporting cast:** transparent 4×2 sprite atlas with separated complete figures: panicked gray mouse carrying toilet roll; muscular purple-clad gym lifter with mohawk and bent arms, no barbell; green trainer with swept hair and clipboard; yellow gym runner with ponytail; blue/red nervous royal guard with spear; purple butler with tray/prune; red/gold trumpeter; empty silver armour. No labels or background.
- **Props:** transparent 2×2 atlas: overhead white toilet with plain turquoise bowl water; smiling crowned cartoon turd; gold five-candle chandelier; jeweled gold crown. Separate complete silhouettes with no text or background. The whirlpool and turd's orbit are animated at runtime.

Character motion combines expression changes with sprite deformation, breathing, shoulder/fist movement and alternating heel motion. Supporting sprites move along staged paths; cupboard doors, falling tiles/paper, sink jets, flying props, barbell, cracks and particle effects are animated separately. This is illustrated sprite animation, not skeletal 3D animation.


## Gym interaction update prompt set

All four new assets were created using the built-in image generation tool, with the existing gym hero/cast as references. Each prompt required genuine transparent alpha, matching bold dark outlines and saturated handpainted 1990s arcade artwork, and no text, labels, backgrounds or scanlines.

- **Deflated hero:** same adult bald moustached man, red sweatband/wristbands, black vest, gold belt, blue shorts at ankles and shoes, on the same white toilet. Replace the enormous muscles with thin arms, narrow shoulders and a loose sagging oversized vest. Normal-size head, relieved sheepish smile, full frontal hair-to-shoes silhouette. Preserve the lower-body/toilet scale.
- **Lifter:** 3×2 atlas of the purple-clad mohawked adult. First row: low, half and high barbell curls, both hands visibly gripping the bar and changing elbow angles. Second row: crouched weight set-down; two panic-running poses to the left without the bar. Consistent scale and baseline, transparent gutters.
- **Runner:** 3×2 atlas of the adult yellow-clad ponytailed runner. Four full-body treadmill stride phases with changing knees and arm positions; a startled loss-of-balance pose; a seated floor-collapse pose with dazed cartoon eyes. No equipment baked into the sprites. The fourth stride is mirrored at render time to maintain direction.
- **Trainer:** 3×2 atlas of the adult green-clad trainer. Writing on clipboard; looking toward the lifter and coaching; startled empty-handed recoil; two rightward escape poses without clipboard; a separate clipboard-and-pen prop. Consistent identity, full-body scale and baseline.

Pose silhouettes are alpha-bounded in `rects.json`; rendering scales them against a common standing height so crouching and seated poses remain shorter rather than stretching back to standing size.


## Sumo and plunger expansion — built-in image generation

Final project assets are `assets/retro/sumo.png` / `.webp` (three-pose transparent atlas) and `assets/retro/bathhouse.png` / `.webp`. The plunger is a code-drawn wooden handle and rubber cup, layered over the existing toilet prop, animated target rings, water and removable paper/clog pieces.

Prompt set:
- **Bathhouse:** front-facing open-air Japanese bathhouse terrace, snowy Mount Fuji high in the center, blue sky, cherry blossoms, red lanterns, warm wooden deck, turquoise pools on both sides, bucket and sandals at left, bamboo at right; empty central foreground for the seated hero. No people, toilet, text or UI. Refinement used the existing bathroom as a style reference: simplify realistic textures into large readable cartoon shapes, bold dark outlines and bright cel shading while preserving the composition.
- **Sumo:** three equal columns, genuine transparent background; same huge round adult wrestler on a tiny white toilet, orange mawashi covering the groin, black topknot, sandals, fists on knees. Calm, strained and wild expressions at matching size/baseline. Refinement used the bodybuilder atlas as a style reference: larger head, enormous white oval cartoon eyes, button nose, oversized grin/gritted teeth, thick eyebrows, smooth simplified shapes and bright arcade highlights; no moustache, realistic skin texture, background or text.

Sources were generated with the built-in image tool, copied into this project and exported to WebP with alpha-bounded atlas rectangles. Synthesized coach cues are `voice-pace-it.wav`, `voice-faster.wav`, `voice-hold.wav`, `voice-push.wav` and `voice-breathe.wav`, rendered offline using the same processed eSpeak NG voice as the countdown.
