* https://github.com/astral-sh/uv
* https://docs.astral.sh/uv/getting-started/features/#tools

* Install uv
    * https://docs.astral.sh/uv/getting-started/installation/

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

* Prep

```
brew install ffmpeg 
uv init generate-notes

# for generating MP3 files
uv add pydub

# for generating MIDI
uv add mido

# For MIDI playback (through MIDI controller / Garage Band)
uv add python-rtmidi

# For direct MIDI playback
uv add pygame
```

## Using uv

```
# uv run ...
# uv sync
uv run generate-mp3s.py

uv run generate-midi.py
uv run verify-midi-duration.py
uv run play-midi-garage-band.py

# Or
uv run play-midi-pygame.py
```

## Putting it all together

* Generate and verify the midi file

```
uv run generate-midi.py
uv run verify-midi-duration.py
```

* Open the midi file in Garage Band and choose the instrument you want
* Click Share and Export the song to disk, saving as WAV file

* Open the WAV file in Audacity and Export Audio (Select "Trim blank space before first clip") to save as WAV again

* Chop the WAV file into mp3s

```
uv run chop-wav-to-mp3.py generated-midi/15_notes_c_major_classical_acoustic_guitar.wav
```

* Test the MP3s

```
uv run play-mp3s.py generated-midi/chopped_segments
```
