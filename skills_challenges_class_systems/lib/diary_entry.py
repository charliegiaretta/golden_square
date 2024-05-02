import math

class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents

    def count_words(self):
        return len (self.contents.split())

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        pass
