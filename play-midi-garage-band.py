import mido
from mido import MidiFile

def play_midi(file_path):
    # List all available output ports
    print("Available MIDI output ports:")
    for port_name in mido.get_output_names():
        print(port_name)

    # Select the correct port (replace "GarageBand" with the correct port name)
    port_name = "GarageBand Virtual In"  # Replace this with the actual port name for GarageBand
    with mido.open_output(port_name) as port:
        # Load the MIDI file
        midi = MidiFile(file_path)
        print(f"Playing MIDI file: {file_path}")

        # Play each message in the MIDI file
        for msg in midi.play():
            if not msg.is_meta:
                port.send(msg)

    print("Playback finished.")

# Replace '15_notes_c_major_scale.mid' with your MIDI file path
midi_file_path = "generated-midi/15_notes_c_major_scale.mid"
play_midi(midi_file_path)
