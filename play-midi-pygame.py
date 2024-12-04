import pygame
import time

def play_midi(file_path):
    # Initialize pygame mixer for MIDI playback
    pygame.init()
    pygame.mixer.init()

    # Load the MIDI file
    try:
        pygame.mixer.music.load(file_path)
        print(f"Playing MIDI file: {file_path}")
    except pygame.error as e:
        print(f"Error loading MIDI file: {e}")
        return

    # Play the MIDI file
    pygame.mixer.music.play()

    # Wait for the playback to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print("Playback finished.")
    pygame.mixer.quit()

# Replace '15_notes_c_major_scale.mid' with your MIDI file path
midi_file_path = "generated-midi/15_notes_c_major_scale.mid"
play_midi(midi_file_path)
