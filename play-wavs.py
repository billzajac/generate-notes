import os
import sys
import time
import pygame

def play_files_in_folder(folder_path):
    # Initialize the pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Get a list of WAV files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".wav")]
    if not files:
        print(f"No WAV files found in folder: {folder_path}")
        sys.exit(1)

    # Play each file
    for file_name in sorted(files):  # Sort for sequential playback
        file_path = os.path.join(folder_path, file_name)
        print(f"Now playing: {file_name}")

        # Load and play the file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

    print("All files played.")
    pygame.mixer.quit()

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python play_wav_files.py <folder_path>")
        sys.exit(1)

    # Get the folder path from arguments
    folder_path = sys.argv[1]

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        sys.exit(1)

    # Play the files in the folder
    play_files_in_folder(folder_path)
