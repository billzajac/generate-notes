import numpy as np
from pydub import AudioSegment

def generate_seamless_shepard_tone(duration=10, base_frequency=110, num_octaves=6, sample_rate=44100):
    """
    Generate a Shepard Tone that loops seamlessly by starting and ending sine waves at the same point.

    :param duration: Duration of the tone in seconds.
    :param base_frequency: Base frequency (e.g., 110 Hz for A2).
    :param num_octaves: Number of octaves to include in the illusion.
    :param sample_rate: Sampling rate in Hz.
    :return: An AudioSegment containing the Shepard Tone.
    """
    # Time array for one loop cycle
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Shepard tone waveform
    shepard_wave = np.zeros_like(t)

    for n in range(num_octaves):
        # Frequency for this octave
        frequency = base_frequency * (2 ** n)

        # Align sine waves so they start and end at the same phase
        phase = 2 * np.pi * frequency * t
        sine_wave = np.sin(phase)  # Starts at 0 and progresses cyclically

        # Cyclic amplitude modulation
        amplitude = np.sin(2 * np.pi * (t / duration - n / num_octaves)) ** 2

        # Apply amplitude modulation to the sine wave
        sine_wave *= amplitude

        # Add this sine wave to the Shepard tone
        shepard_wave += sine_wave

    # Normalize the waveform
    shepard_wave /= np.max(np.abs(shepard_wave))

    # Force the start and end points to match exactly
    shepard_wave[-1] = shepard_wave[0]

    # Convert to 16-bit PCM format
    shepard_wave_pcm = (shepard_wave * 32767).astype(np.int16)

    # Convert to pydub AudioSegment
    audio = AudioSegment(
        shepard_wave_pcm.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,  # 16-bit audio
        channels=1       # Mono
    )

    return audio

if __name__ == "__main__":
    duration = 10  # Duration of one loop cycle in seconds
    base_frequency = 110  # Lower starting frequency (A2)
    output_file = "seamless_shepard_tone_aligned.wav"

    # Generate the Shepard Tone
    shepard_tone = generate_seamless_shepard_tone(duration=duration, base_frequency=base_frequency)

    # Export the audio
    shepard_tone.export(output_file, format="wav")
    print(f"Seamless Shepard Tone saved as {output_file}")
