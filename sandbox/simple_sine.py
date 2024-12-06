import numpy as np
from pydub import AudioSegment

def generate_simple_looping_tone(duration=10, frequency=440, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    sine_wave_pcm = (sine_wave * 32767).astype(np.int16)

    return AudioSegment(
        sine_wave_pcm.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,
        channels=1
    )

# Generate and save a simple tone
simple_tone = generate_simple_looping_tone()
simple_tone.export("simple_looping_tone.wav", format="wav")
