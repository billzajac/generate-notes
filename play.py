import os
import sys
import time
from pydub import AudioSegment
from pydub.playback import play

def play_audio_files_in_directory(directory):
    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    # Get a list of all .wav and .mp3 files in the directory
    audio_files = [f for f in os.listdir(directory) if f.endswith(('.wav', '.mp3'))]
    if not audio_files:
        print(f"No .wav or .mp3 files found in directory '{directory}'.")
        return

    # Play each file in order
    for audio_file in sorted(audio_files):
        file_path = os.path.join(directory, audio_file)
        print(f"Now playing: {audio_file}")

        # Load the audio file
        try:
            audio = AudioSegment.from_file(file_path)
            play(audio)  # Play the audio
        except Exception as e:
            print(f"Could not play '{audio_file}': {e}")

    print("All audio files played.")

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python play_audio_files.py <directory_path>")
        sys.exit(1)

    # Get the directory from the command-line argument
    directory_path = sys.argv[1]

    # Play the audio files in the directory
    play_audio_files_in_directory(directory_path)
