import pretty_midi
import fnmatch
import os


midi_dir = './RWC-MDB-C-2001-MIDIs'

for file in os.listdir(midi_dir):
        if os.path.isfile(midi_dir + "/" + file):
            if fnmatch.fnmatch(file, '*.mid') or fnmatch.fnmatch(file, '*.MID'):
                # Load MIDI file into PrettyMIDI object
                midi_data = pretty_midi.PrettyMIDI(midi_dir +  "/" + file)
                new_midi = pretty_midi.PrettyMIDI(resolution=220, initial_tempo=120.0)

                # Shift all notes up by 5 semitones
                for instrument in midi_data.instruments:
                    for note in instrument.notes:
                        note.velocity = 85
                    new_midi.instruments.append(instrument)

                new_midi.write('./NEW_MIDIs/' + file)