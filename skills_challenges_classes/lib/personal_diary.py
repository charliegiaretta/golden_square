class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f'{self.title}: {self.contents}'
    
    def count_words(self):
        words = self.title.split() + self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        words = self.contents.split()
        count = len(words) / wpm
        return count 

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        x = wpm * minutes
        return ' '.join(words[:x])

