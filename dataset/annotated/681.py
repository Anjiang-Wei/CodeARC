def transpose_song(song: list[str], interval: int) -> list[str]:
    altern = {"Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#"}
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    # Transpose each note by the given interval
    return [notes[(notes.index(altern.get(note, note)) + interval) % 12] for note in song]

