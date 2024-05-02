"""
As an office worker
So I can record useful information
I want to be able to create a text note

As an office worker
So I can carry all my useful information
I want to keep all my notes in a notebook.

As an office worker
So I can categorise a note
I want to be able to add a tag (only one tag) to a note

As an office worker
So I can find notes on a certain topic
I want to be able to search for all the notes with a specific tag
"""

class Notebook():
    def __init__(self):
        notebook = {}

    def create(self, note):
        return self.notebook.append(note)
    

        