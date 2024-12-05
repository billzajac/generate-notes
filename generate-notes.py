import os
import sys
from mido import MidiFile, MidiTrack, Message
import subprocess
from pydub import AudioSegment

# Ensure output folder exists
OUTPUT_FOLDER = "generated/notes"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Generate a MIDI file with a single note
def create_midi(note, duration_ticks, filename):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Classical Acoustic Guitar - program 24
    # Trumpet - program 56
    # Celesta - program 8
    # Music Box - program 10
    # Glockenspiel - program 9
    # Vibraphone - program 11
    # Tinkle Bell - program 112
    # Harp - program 46

    track.append(Message('program_change', program=10, time=0))

    # Add note-on and note-off messages
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration_ticks))

    # Save MIDI file
    midi.save(filename)

# Convert MIDI to MP3 using FluidSynth and amplify the audio
def midi_to_mp3(midi_file, mp3_file, soundfont_path, amplification_db=0):
    # Use FluidSynth to render the MIDI file to a WAV
    wav_file = mp3_file.replace(".mp3", ".wav")
    subprocess.run([
        "fluidsynth",
        "-g", "2.0", # Increase gain (maix is 2.0)
        "-ni", soundfont_path,
        midi_file,
        "-F", wav_file,
        "-r", "44100"
    ])

    # Convert WAV to MP3 and trim to 100ms
    audio = AudioSegment.from_file(wav_file)
    normalized_audio = audio.normalize()  # Normalize to avoid clipping

    # Amplify the audio
    amplified_audio = normalized_audio + amplification_db  # Increase volume by specified dB
    trimmed_audio = amplified_audio[:600]  # Trim to 100ms

    # Export amplified and trimmed audio to MP3
    trimmed_audio.export(mp3_file, format="mp3")
    os.remove(wav_file)  # Clean up the intermediate WAV file

# Generate notes and save as MP3
def generate_notes(soundfont_path):
    # Define note parameters
    duration_ms = 100
    ticks_per_beat = 480
    bpm = 120
    duration_ticks = int((duration_ms / 1000) * ticks_per_beat * (bpm / 60))

    # Define the starting note (C4) and generate 16 ascending notes
    starting_note = 60
    notes = [starting_note + i for i in range(16)]

    for i, note in enumerate(notes):
        midi_file = os.path.join(OUTPUT_FOLDER, f"note_{i+1:02d}.mid")
        mp3_file = os.path.join(OUTPUT_FOLDER, f"note_{i+1:02d}.mp3")

        print(f"Generating Note {i + 1}: MIDI={midi_file}, MP3={mp3_file}")
        create_midi(note, duration_ticks, midi_file)
        midi_to_mp3(midi_file, mp3_file, soundfont_path)
        os.remove(midi_file)  # Clean up the intermediate MIDI file

    # Generate dissonant flat note
    dissonant_note = starting_note - 2  # Example: B flat if starting_note is C4
    dissonant_midi_file = os.path.join(OUTPUT_FOLDER, "note_flat.mid")
    dissonant_mp3_file = os.path.join(OUTPUT_FOLDER, "note_flat.mp3")

    print(f"Generating Dissonant Flat Note: MIDI={dissonant_midi_file}, MP3={dissonant_mp3_file}")
    create_midi(dissonant_note, duration_ticks, dissonant_midi_file)
    midi_to_mp3(dissonant_midi_file, dissonant_mp3_file, soundfont_path)
    os.remove(dissonant_midi_file)  # Clean up the intermediate MIDI file

    print("Notes generation complete!")

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python generate_notes.py <path_to_soundfont.sf2>")
        sys.exit(1)

    # Get the SoundFont file path
    soundfont_path = sys.argv[1]

    # Check if the SoundFont file exists
    if not os.path.isfile(soundfont_path):
        print(f"Error: SoundFont file '{soundfont_path}' not found.")
        sys.exit(1)

    # Generate notes
    generate_notes(soundfont_path)
