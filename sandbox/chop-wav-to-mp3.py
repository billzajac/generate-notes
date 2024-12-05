import os
from pydub import AudioSegment

def chop_wav_to_mp3(input_file, output_folder, segment_duration_ms=100, steps=15):
    # Load the WAV file
    audio = AudioSegment.from_file(input_file)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Chop the audio into segments
    for i in range(steps):
        start_time = i * segment_duration_ms
        end_time = start_time + segment_duration_ms

        # Extract the segment
        segment = audio[start_time:end_time]

        # Save the segment as an MP3
        output_file = os.path.join(output_folder, f"segment_{i+1:02d}.mp3")
        segment.export(output_file, format="mp3")
        print(f"Saved: {output_file}")

    print("Chopping complete!")

if __name__ == "__main__":
    import sys

    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python chop_wav_to_mp3.py <path_to_wav_file>")
        sys.exit(1)

    # Input WAV file
    input_wav = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(input_wav):
        print(f"Error: File '{input_wav}' not found.")
        sys.exit(1)

    # Define the output folder
    output_dir = os.path.join(os.path.dirname(input_wav), "chopped_segments")

    # Run the chopping function
    chop_wav_to_mp3(input_wav, output_dir)
