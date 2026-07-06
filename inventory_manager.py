import json
from notes import Note

class NotesManager:
    def __init__(self):
        self.notes = []
    def add_note(self, note):
        self.notes.append(note)
    def show_notes(self):
        for i,note in enumerate(self.notes, start=1):
            print(f"{i}. {note.title}: {note.text}")
    def delete_note(self, index):
        self.notes.pop(index-1)