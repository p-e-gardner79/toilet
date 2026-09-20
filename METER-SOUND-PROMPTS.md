# Reactive relief-meter sounds

Generate these as separate sound effects, not spoken dialogue. Keep them dry and isolated, without music, voices, room ambience or a final toilet splash. Clean WAV preferred; MP3 is fine. These support the existing character/event effects rather than replacing them.

## 1. meter-tap — 0.15 to 0.25 seconds

> One short, playful rubbery bubble-pop with a soft squishy plunk and a tiny rounded bass wobble. A tactile reward for pressing a button in a colourful 1990s cartoon arcade game. Cute, bouncy and satisfying, not realistic or disgusting. Immediate attack, very short clean tail. Single isolated sound, no repeated sequence, no speech, music, ambience or reverb.

The game triggers this only when a tap increases relief. Slow taps produce separated pops; fast taps produce a quicker bubbling rhythm. Playback pitch rises slightly with meter progress. Supply one sound, not a prerecorded slow/fast tapping sequence.

## 2. meter-hold — 4-second seamless loop

> A steady, comical build-up of plumbing pressure: soft rubber stretching mixed with low bubbly gurgles and a rounded cartoon creak. Playful tension, like an inflatable cartoon object under pressure. Continuous even intensity and pitch, with no climax. Seamless four-second loop, no opening impact, no ending splash, no silence at the seam. Dry isolated game sound, no music, voice or ambience.

The game loops this only while the player holds the button, gently raises its playback pitch with pressure, and stops it on release, cancellation or pause. Do not bake a rising pitch or climax into the recording: the game controls that in response to the player.

## 3. meter-release — 0.4 to 0.7 seconds

> A short satisfying cartoon pressure-release: a soft pneumatic pfft followed immediately by a cheerful rubbery boing and a tiny clean bubble pop. Positive, bouncy arcade reward for perfect timing. Rounded, warm and humorous, not harsh, explosive or gross. One isolated effect, no toilet splash, music, speech, ambience or reverb.

This rewards a correctly timed release. The large final plop keeps its existing separate splash sound.

## Optional later: meter-nearly-full — 1-second seamless loop

> A restrained comical plumbing rattle with tiny nervous bubble ticks, creating playful anticipation. Soft, rhythmic and rounded, no piercing alarm. Seamless one-second loop at steady pitch and volume. No music, voice, splash or room ambience.

Optional near-full tension layer; not currently connected. The first three effects are sufficient for the initial mix.

## Integration

Reserved project filenames: `assets/effect-meter-tap.mp3`, `assets/effect-meter-hold.mp3`, `assets/effect-meter-release.mp3`. Runtime hooks are ready; no placeholder sound is substituted while these assets are absent. Original recordings can be supplied in either WAV or MP3 and converted at import. Effects volume and SOUND apply. Existing speech stays on a separate channel with music ducking.
