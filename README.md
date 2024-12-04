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
