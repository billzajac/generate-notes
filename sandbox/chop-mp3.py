import os
import sys
from pydub import AudioSegment

def chop_mp3(input_file, output_folder, segment_duration_ms=100):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the number of segments
    total_duration = len(audio)  # Total duration in milliseconds
    num_segments = total_duration // segment_duration_ms

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Chop the audio into segments
    for i in range(num_segments):
        start_time = i * segment_duration_ms
        end_time = start_time + segment_duration_ms
        segment = audio[start_time:end_time]

        # Save each segment as an MP3
        output_file = os.path.join(output_folder, f"segment_{i+1:03d}.mp3")
        segment.export(output_file, format="mp3")
        print(f"Saved: {output_file}")

    print("Chopping complete!")

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python chop_mp3.py <path_to_mp3_file>")
        sys.exit(1)

    # Get the input file from the arguments
    input_mp3 = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(input_mp3):
        print(f"Error: File '{input_mp3}' not found.")
        sys.exit(1)

    # Define output folder
    output_dir = os.path.join(os.path.dirname(input_mp3), "chopped_segments")

    # Call the function to chop the MP3
    chop_mp3(input_mp3, output_dir)
