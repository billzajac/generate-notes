import os
import librosa
import numpy as np
from pydub import AudioSegment

def chop_wav_by_notes(input_file, output_folder):
    # Load the audio file
    y, sr = librosa.load(input_file, sr=None, mono=True)

    # Detect onsets (note beginnings)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, backtrack=True)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    print(f"Detected onsets: {onset_times}")

    # Convert WAV to AudioSegment for precise chopping
    audio = AudioSegment.from_file(input_file)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Chop audio at each onset
    for i, start_time in enumerate(onset_times[:-1]):
        end_time = onset_times[i + 1]
        start_ms = int(start_time * 1000)  # Convert to milliseconds
        end_ms = int(end_time * 1000)  # Convert to milliseconds

        segment = audio[start_ms:end_ms]
        output_file = os.path.join(output_folder, f"note_{i+1:03d}.wav")
        segment.export(output_file, format="wav")
        print(f"Saved: {output_file}")

    # Handle the last segment
    last_start_time = int(onset_times[-1] * 1000)
    last_segment = audio[last_start_time:]
    last_output_file = os.path.join(output_folder, f"note_{len(onset_times):03d}.wav")
    last_segment.export(last_output_file, format="wav")
    print(f"Saved: {last_output_file}")

    print("Chopping complete!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python chop_wav_by_notes.py <path_to_wav_file>")
        sys.exit(1)

    input_wav = sys.argv[1]

    if not os.path.isfile(input_wav):
        print(f"Error: File '{input_wav}' not found.")
        sys.exit(1)

    output_dir = os.path.join(os.path.dirname(input_wav), "chopped_notes")
    chop_wav_by_notes(input_wav, output_dir)
