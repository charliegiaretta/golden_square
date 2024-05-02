from lib.diary_entry import DiaryEntry

"""
DiaryEntry is constructed with a Title and Contents
"""
def test_diary_entry_constructs():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title == "My Title"
    assert entry.contents == "My Contents"