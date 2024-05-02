from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor

"""
When I add multiple diary entires
And i call PhoneNumberExtractor #extract
I get a list of phone numbers from all diary entries
"""
def test_extracts_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000001")
    entry_2 = DiaryEntry("My Title 2", "My friend is 07800000002")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000", "07800000001", "07800000002"}

"""
When I add multiple diary entires
And i call PhoneNumberExtractor #extract
It ignores duplicate numbers
"""
def test_ignores_duplicate_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000000")
    entry_2 = DiaryEntry("My Title 2", "My friend is 07800000000")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000"}

"""
When I add multiple diary entires
And I call PhoneNumberExtractor #extract
It ignores invalid phone numbers
"""
def test_ignores_invalid_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 0780000000000 and07800000000 and 0780000000")
    entry_2 = DiaryEntry("My Title 1", "My friend is 07800 230002")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()

"""
When I add no diary entires
And I call PhoneNumberExtractor #extract
It returns an empty list
"""
def test_with_no_entries_returns_empty_list():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    extractor.extract() == []