import pytest
from lib.diary import Diary

"""
Inititally has an empty list of diary entries
"""
def test_initially_has_empty_list_of_diary_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially, word count is zero
"""
def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
Inititally, reading time should raise an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"

"""
Initially find_best_entry_for_reading_time should raise error
"""
def test_find_best_entry_for_reading_time_initially_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"