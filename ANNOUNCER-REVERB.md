# Arcade announcer with short arena reverb

The active voice comes from the two supplied September 20 Arcade (energetic) recordings. Originals are preserved unchanged in `assets/announcer-originals-v2/`. The earlier voice assets remain archived; the active twelve MP3 cues have been replaced.

The first file is split into slow down, nice and steady/that's it, faster/faster, get ready, push and hold, keep holding/you've got this, release, and beautiful/what a relief. The separate countdown supplies three/two/one/go. Cut points use local word transcription and measured silent gaps; no recordings were uploaded for processing.

Each cue has a centered dry voice plus low-level stereo convolution reverb: a roughly 19ms initial gap followed by dense decaying reflections. Normal cues use a 280ms tail; hold, release and go use 360ms. Peak levels are kept below clipping. Speech is neither pitch-shifted nor time-stretched. The manifest lists exact segment boundaries, tail lengths and resulting durations.

The hold section lasts 5.6 seconds so the drawn-out push/hold and subsequent encouragement can both finish. The maximum held-pressure reward stays 14 relief, and the 35-second round limit remains. Music ducking now follows the replacement clip durations. One announcer cue plays at a time; number clips fit their one-second countdown slots. The full GO finishes before the first coaching cue begins.

Listen without playing:
- `preview/announcer-reverb.mp3`: the complete first performance with the reverb treatment.
- `preview/countdown-reverb.mp3`: the complete countdown with reverb, at its original pacing. In the game the separated numbers are synchronized to one-second visual beats.

All processed clips are embedded into the offline game. No audio engine installation or network service is required to play.

Mix adjustment: announcer playback gain reduced to 62% of its previous level (about -4.2 dB). During speech, music retains 80% of its normal level instead of 38%, so the soundtrack stays present. Effects-volume controls still apply to the announcer.

