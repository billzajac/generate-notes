import os
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

# Define the starting note and the intervals for the C major scale
starting_note = 60  # C4 in MIDI notation
scale_intervals = [2, 2, 1, 2, 2, 2, 1]  # Whole and half steps in C major scale

# Generate the first 15 notes of the ascending C major scale
ascending_notes = [starting_note]
for _ in range(14):  # Generate the next 14 notes
    next_note = ascending_notes[-1] + scale_intervals[(len(ascending_notes) - 1) % len(scale_intervals)]
    ascending_notes.append(next_note)

NOTE_TICKS = 96  # 100ms at 120 BPM (480 ticks per beat)
# Duration of each note in ticks (assuming 480 ticks per beat, 100ms ~= 1/10th of a beat at 120 BPM)
# NOTE_TICKS = 480 // 10

# Create a new MIDI file and track
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Add a tempo message (120 BPM)
track.append(MetaMessage('set_tempo', tempo=bpm2tempo(120)))

# Add the notes to the track
for note in ascending_notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))  # Note on
    track.append(Message('note_off', note=note, velocity=64, time=NOTE_TICKS))  # Note off

# Define the output folder and file name
output_folder = "generated-midi"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
midi_filename = os.path.join(output_folder, "15_notes_c_major_scale.mid")

# Save the MIDI file
midi_file.save(midi_filename)

print(f"MIDI file saved as {midi_filename}")
