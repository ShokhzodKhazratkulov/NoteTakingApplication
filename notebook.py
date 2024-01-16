from note import Note
import csv
from datetime import datetime

class Notebook:
    def __init__(self):
        self.notes_list = []

    def add_notes(self, title, content):
        """Add Note Method: Adds a new note to the list of notes."""
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(title, content, creation_date)
        self.notes_list.append(new_note)
        self.save_notes_to_file(new_note)

    def remove_note(self, title):
        """Remove Note Method: Deletes a note based on its title."""
        note_to_remove = next((note for note in self.notes_list if note.title == title), None)
        if note_to_remove:
            self.notes_list.remove(note_to_remove)
            self.remove_notes_from_file(note_to_remove)

    def display_all_notes(self):
        for note in self.notes_list:
            note.display_content()

    def save_notes_to_file(self, note):
        """Save Notes Method: Writes notes to a file or database for storage."""
        file_name = "saved_files.csv"
        with open(file_name, mode="a", newline='') as data_file:
            data = csv.writer(data_file)
            data.writerow([note.title, note.content, note.creation_date])

    def remove_notes_from_file(self, note):
        """Remove Notes from File Method: Removes a note from the file."""
        file_name = "saved_files.csv"
        data_to_remove = [note.title, note.content, note.creation_date]

        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = [row for row in reader if row != data_to_remove]

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)



