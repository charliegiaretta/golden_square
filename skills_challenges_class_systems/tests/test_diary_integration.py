from lib.diary import *
from lib.diary_entry import *

"""
When we add two diary entries
We get the diary entries back in a list
"""
def test_adds_and_lists_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given I add two diary entries
And I call count words
I get the sum of all words in contents of diary entries
"""
def test_count_words_of_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    entry_2 = DiaryEntry("My Title 2", "two three")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 4

"""
Given I add two diary entries with a total length of 5
And I call reading_time with a wpm of 2
Then the total reading time should be 3
"""
def test_reading_time_of_all_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    entry_2 = DiaryEntry("My Title 2", "three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
Given I add two diary entries, one long and one short,
I call find_best_entry_for_reading_time
With a wpm and minutes that means I can only read the short one
Then find_best_for_reading_time returns the shorter one
"""
def test_find_best_for_reading_time_returns_the_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    entry_2 = DiaryEntry("My Title 2", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add a diary entry
And I call find_best_entry_for_reading_time
With wpm and minutes that I can read entry in time
Then find_best_entry_for_reading_time_fits_in_time returns that entry
"""
def test_find_best_for_reading_time_returns_the_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add a diary entry
And I call find_best_entry_for_reading_time
With wpm and minutes that I cannot read entry in time
Then find_best_entry_for_reading_time_fits_in_time returns None
"""
def test_find_best_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given I add two diary entries
And I call find_best_entry_for_reading_time
With wpm and minutes that I could read both
Then find_best_entry_for_reading_time_fits_in_time returns the longer one
"""
def test_find_best_entry_for_reading_time_returns_the_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three")
    entry_2 = DiaryEntry("My Title 2", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2