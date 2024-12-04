import os
from pydub.generators import Sine
from pydub import AudioSegment

# Define the frequencies of the C major scale
C_MAJOR_SCALE = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

# Length of each note in milliseconds
NOTE_DURATION = 100

# Subfolder to save the generated files
output_folder = "generated-mp3s"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate and save 8 notes
for i in range(8):
    # Cycle through the scale to get the current note
    freq = C_MAJOR_SCALE[i % len(C_MAJOR_SCALE)]

    # Generate a sine wave for the note
    tone = Sine(freq).to_audio_segment(duration=NOTE_DURATION)

    # Create the filename and full path
    filename = f"note_{i+1:02d}_{freq:.2f}Hz.mp3"
    filepath = os.path.join(output_folder, filename)

    # Export the note as an MP3 file
    tone.export(filepath, format="mp3")
    print(f"Saved {filepath}")
