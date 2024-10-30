import os
import subprocess
import re
import mido
import time
import signal
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
ENHARMONIC_EQUIVALENTS = {
    'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#', 'Cb': 'B', 'Fb': 'E'
}
KEY_PATTERN = re.compile(r'_([A-G]#?m?b?)(?=(_|\d|\w|$|b))_', re.IGNORECASE)

def get_note_name(midi_note):
    note = NOTE_NAMES[midi_note % 12]
    return ENHARMONIC_EQUIVALENTS.get(note, note)

def identify_chord(notes):
    notes = [get_note_name(note) for note in notes]
    if len(notes) < 3:
        return "Unknown Chord"
    
    root, third, fifth = notes[:3]
    root_note_number = NOTE_NAMES.index(root)
    third_note_number = NOTE_NAMES.index(third)
    fifth_note_number = NOTE_NAMES.index(fifth)

    minor_third = (root_note_number + 3) % 12
    major_third = (root_note_number + 4) % 12
    perfect_fifth = (root_note_number + 7) % 12

    if (third_note_number == minor_third and fifth_note_number == perfect_fifth):
        return f"{root.lower()}m"  # Ensure minor keys have "m" in lowercase
    elif (third_note_number == major_third and fifth_note_number == perfect_fifth):
        return f"{root.upper()}"  # Major keys do not have 'm' and are uppercase
    
    return "Unknown Chord"

def get_selected_files():
    try:
        script = '''
        tell application "Finder"
            set selectedFiles to selection
            set filePaths to {}
            repeat with f in selectedFiles
                set end of filePaths to (POSIX path of (f as alias))
            end repeat
        end tell
        return filePaths
        '''
        selected_files = subprocess.check_output(['osascript', '-e', script])
        return selected_files.decode('utf-8').strip().split(", ")
    except subprocess.CalledProcessError:
        logger.warning("No files selected in Finder.")
        return None

def chord_to_filename_format(chord):
    parts = chord.split()
    root = parts[0].upper()  # Ensure the root is uppercase
    if len(parts) > 1 and parts[1].lower() == 'm':  # Check for minor
        return f"_{root}m_"  # Minor keys: "_Am" with "m" lowercase
    else:
        return f"_{root}_"  # Major keys: "_F" in uppercase

def replace_key_in_filename(file_name, new_key):
    match = KEY_PATTERN.search(file_name)
    
    if match:
        old_key = match.group()
        new_key_format = chord_to_filename_format(new_key)

        # Replace A# with Bb for major keys
        if new_key == 'A#':
            new_key_format = f"_{'Bb'}_"
        # Replace A# minor with Bb minor
        elif new_key == 'A#m':
            new_key_format = f"_{'Bbm'}_"

        new_file_name = file_name[:match.start()] + file_name[match.start():].replace(old_key, new_key_format, 1)
        
        # Change uppercase "M" to lowercase "m" for minor keys
        if "M" in new_file_name:
            new_file_name = new_file_name.replace("M", "m")
        
        return new_file_name
    return None

def rename_selected_files(new_key):
    selected_files = get_selected_files()
    
    if selected_files:
        for selected_file in selected_files:
            if os.path.isfile(selected_file):
                base, ext = os.path.splitext(selected_file)
                if new_key != "Unknown Chord":
                    new_name = replace_key_in_filename(base, new_key)
                    if new_name:
                        print(f"DEBUG: New filename generated: {new_name}")  # Debug statement
                        new_full_name = f"{new_name}{ext}"
                        os.rename(selected_file, new_full_name)
                        logger.info(f"Renamed {selected_file} to {new_full_name}")
                else:
                    logger.warning(f"Chord was not recognized. Skipping renaming for {selected_file}.")

def listen_midi():
    logger.info("MIDI listener initialized.")
    try:
        with mido.open_input() as inport:
            active_notes = set()
            chord_start_time = None
            
            while True:
                for msg in inport.iter_pending():
                    if msg.type == 'note_on' and msg.velocity > 0:
                        active_notes.add(msg.note)
                    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                        active_notes.discard(msg.note)

                if len(active_notes) == 3:
                    if chord_start_time is None:
                        chord_start_time = time.time()

                    elapsed_time = time.time() - chord_start_time
                    if elapsed_time >= 1:
                        sorted_notes = sorted(active_notes)
                        chord = identify_chord(sorted_notes)
                        rename_selected_files(chord)
                        chord_start_time = None
                        active_notes.clear()
                else:
                    chord_start_time = None  # Reset timer if not holding 3 notes

    except Exception as e:
        logger.error(f"An error occurred while listening for MIDI input: {e}")

def signal_handler(sig, frame):
    logger.info("Exiting the program gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    listen_midi()
