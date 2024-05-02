from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.readable_entry_extractor import ReadableEntryExtractor
"""
When I add one diary entry
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns that diary entry
"""
def test_gets_single_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_1

"""
When I add one diary entry that does not fit in the time
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns None
"""
def test_returns_none_if_entries_do_not_fit_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == None

"""
When I add multiple diary entries, one readable
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns that diary entry
"""
def test_returns_readable_out_of_readable_and_unreadable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five")
    entry_2 = DiaryEntry("My Title 1", "one two three four")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_2

"""
When I add multiple diary entries, multiple readable
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns the longest readable one
"""
def test_gets_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four")
    entry_2 = DiaryEntry("My Title 1", "one two three four five")
    entry_3 = DiaryEntry("My Title 1", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=3) == entry_2

"""
When I add no diary entries
and I call ReadableEntryExtractor #extract
It returns None
"""
def test_with_no_entries_returns_none():
    diary = Diary()
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == None
