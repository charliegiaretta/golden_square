from lib.personal_diary import *

"""
When title and contents given
Returns a formatted diary entry
"""
def test_format_diary_entry():
    diary_entry = DiaryEntry(title='My Title', contents='These are the contents')
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

"""
When title and contents given
Count the words in the diary entry
"""
def test_count_diary_entry_words():
    diary_entry = DiaryEntry(title='My Title', contents='These are the contents')
    result = diary_entry.count_words()
    assert result == 6

"""
When contents given
Provide an float representing amount of time it will take if wpm is 1
"""
def test_diary_entry_reading_time():
    diary_entry = DiaryEntry(title='My Title', contents='These are the contents')
    result = diary_entry.reading_time(1)
    assert result == 4.0

"""
When contents given
Provide a chunk of contents the user could read based on a wpm 
of 2 and minutes as 1
"""
def test_diary_entry_reading_chunk():
    diary_entry = DiaryEntry(title="My Title", contents="one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == 'one two'

"""
When contents given
Provide a chunk of contents the user could read based on a wpm 
of 2 and minutes as 3
"""
def test_diary_entry_reading_chunk():
    diary_entry = DiaryEntry(title="My Title", contents="one two three four five six")
    result = diary_entry.reading_chunk(2, 3)
    assert result == 'one two three four five six'