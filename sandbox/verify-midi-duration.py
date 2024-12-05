from mido import MidiFile

# Load the MIDI file
midi_file = MidiFile("generated-midi/15_notes_c_major_scale.mid")

# Calculate the duration in seconds
total_duration = sum(msg.time for msg in midi_file.tracks[0]) / midi_file.ticks_per_beat * (60 / 120)  # Assuming 120 BPM

print(f"Total duration of the MIDI file: {total_duration:.2f} seconds")
