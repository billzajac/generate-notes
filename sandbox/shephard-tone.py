import numpy as np
from scipy.io import wavfile

def generate_shepard_tone(duration=5, sample_rate=44100):
    """
    Generate a Shepard tone that creates a clearer illusion of continuously ascending pitch.
    
    Parameters:
    duration (float): Duration of the tone in seconds
    sample_rate (int): Sample rate of the audio
    
    Returns:
    numpy.ndarray: The generated Shepard tone waveform
    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create frequencies spanning several octaves
    base_freq = 50  # Lower base frequency for better audibility
    num_octaves = 6
    frequencies = base_freq * 2**np.arange(num_octaves)
    
    # Initialize empty array for the final waveform
    shepard_tone = np.zeros_like(t)
    
    # Speed of ascent (adjusted for smoother transition)
    speed = 1.0
    
    for freq in frequencies:
        # More gradual frequency increase
        instant_freq = freq * 2**(speed * t / duration)
        phase = 2 * np.pi * freq * (2**(speed * t / duration) - 1) / (speed * np.log(2))
        
        # Generate sine wave
        sine_wave = np.sin(phase)
        
        # Calculate amplitude envelope
        # Log position in frequency space, normalized to [0, 1]
        position = (np.log2(instant_freq) - np.log2(base_freq)) % num_octaves
        
        # Smoother amplitude envelope using shifted cosine
        amplitude = 0.5 * (1 + np.cos(2 * np.pi * (position / num_octaves - 0.5)))
        
        # Add to final waveform
        shepard_tone += sine_wave * amplitude
    
    # Normalize the waveform
    shepard_tone = shepard_tone / np.max(np.abs(shepard_tone))
    
    # Apply slight fade in/out to avoid clicks
    fade_samples = int(0.01 * sample_rate)  # 10ms fade
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)
    shepard_tone[:fade_samples] *= fade_in
    shepard_tone[-fade_samples:] *= fade_out
    
    return shepard_tone

# Generate the tone
duration = 5  # shorter duration for tighter loop
sample_rate = 44100
tone = generate_shepard_tone(duration, sample_rate)

# Save as WAV file
wavfile.write('shepard_tone.wav', sample_rate, (tone * 32767).astype(np.int16))
