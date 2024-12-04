import os
from mido import MidiFile, MidiTrack, Message
import subprocess
from pydub import AudioSegment

# Output folder for generated chimes
OUTPUT_FOLDER = "chimes"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Generate a MIDI file with a sequence of notes
def create_midi_sequence(notes, durations, filename, program=56):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Set the instrument (default: trumpet, program 56 in GM)
    track.append(Message('program_change', program=program, time=0))

    # Add the sequence of notes
    for i, note in enumerate(notes):
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=durations[i]))

    # Save the MIDI file
    midi.save(filename)

# Convert MIDI to MP3 using FluidSynth
def midi_to_mp3(midi_file, mp3_file, soundfont_path, amplification_db=5):
    # Render the MIDI file to a WAV file
    wav_file = mp3_file.replace(".mp3", ".wav")
    subprocess.run([
        "fluidsynth",
        "-ni", soundfont_path,
        midi_file,
        "-F", wav_file,
        "-r", "44100"
    ])

    # Load and amplify the audio
    audio = AudioSegment.from_file(wav_file)
    amplified_audio = audio + amplification_db  # Amplify the sound
    trimmed_audio = amplified_audio[:1500]  # Trim to 100ms
    trimmed_audio.export(mp3_file, format="mp3")


    # Clean up intermediate WAV file
    os.remove(wav_file)

# Create celebratory and too-bad chimes
def create_chimes(soundfont_path):
    # Parameters
    ticks_per_beat = 480
    bpm = 120

    # Celebratory chime: upward progression (extended to two octaves)
    celebratory_notes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]  # C4 to C6
    celebratory_duration_ms = 60  # Each note is 60ms
    celebratory_durations = [int((celebratory_duration_ms / 1000) * ticks_per_beat * (bpm / 60))] * len(celebratory_notes)
    celebratory_midi = os.path.join(OUTPUT_FOLDER, "celebratory_chime.mid")
    celebratory_mp3 = os.path.join(OUTPUT_FOLDER, "celebratory_chime.mp3")
    create_midi_sequence(celebratory_notes, celebratory_durations, celebratory_midi)
    midi_to_mp3(celebratory_midi, celebratory_mp3, soundfont_path)
    os.remove(celebratory_midi)
    print(f"Celebratory chime created: {celebratory_mp3}")

    # Ta-da good chime: two long notes (mid to mid)
    tada_good_notes = [72, 72]  # C5 to C3
    tada_good_duration_ms = [300, 800]  # First note 800ms, second note 1200ms
    tada_good_durations = [int((dur / 1000) * ticks_per_beat * (bpm / 60)) for dur in tada_good_duration_ms]
    tada_good_midi = os.path.join(OUTPUT_FOLDER, "tada_good_chime.mid")
    tada_good_mp3 = os.path.join(OUTPUT_FOLDER, "tada_good_chime.mp3")
    create_midi_sequence(tada_good_notes, tada_good_durations, tada_good_midi)
    midi_to_mp3(tada_good_midi, tada_good_mp3, soundfont_path)
    os.remove(tada_good_midi)
    print(f"Ta-da good chime created: {tada_good_mp3}")

    # Ta-da great chime: two long notes (mid to mid)
    tada_great_notes = [79, 84]  # C5 to C3
    tada_great_duration_ms = [300, 800]  # First note 800ms, second note 1200ms
    tada_great_durations = [int((dur / 1000) * ticks_per_beat * (bpm / 60)) for dur in tada_great_duration_ms]
    tada_great_midi = os.path.join(OUTPUT_FOLDER, "tada_great_chime.mid")
    tada_great_mp3 = os.path.join(OUTPUT_FOLDER, "tada_great_chime.mp3")
    create_midi_sequence(tada_great_notes, tada_great_durations, tada_great_midi)
    midi_to_mp3(tada_great_midi, tada_great_mp3, soundfont_path)
    os.remove(tada_great_midi)
    print(f"Ta-da great chime created: {tada_great_mp3}")

    # Too-bad chime: two long notes (high to low)
    too_bad_notes = [67, 48]  # C5 to C3
    too_bad_duration_ms = [300, 800]  # First note 800ms, second note 1200ms
    too_bad_durations = [int((dur / 1000) * ticks_per_beat * (bpm / 60)) for dur in too_bad_duration_ms]
    too_bad_midi = os.path.join(OUTPUT_FOLDER, "too_bad_chime.mid")
    too_bad_mp3 = os.path.join(OUTPUT_FOLDER, "too_bad_chime.mp3")
    create_midi_sequence(too_bad_notes, too_bad_durations, too_bad_midi)
    midi_to_mp3(too_bad_midi, too_bad_mp3, soundfont_path)
    os.remove(too_bad_midi)
    print(f"Too-bad chime created: {too_bad_mp3}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python create_chimes.py <path_to_soundfont.sf2>")
        sys.exit(1)

    # Path to the SoundFont file
    soundfont_path = sys.argv[1]

    # Check if the SoundFont file exists
    if not os.path.isfile(soundfont_path):
        print(f"Error: SoundFont file '{soundfont_path}' not found.")
        sys.exit(1)

    # Generate chimes
    create_chimes(soundfont_path)
