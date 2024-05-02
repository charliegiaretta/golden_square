from lib.diary import Diary

"""
Inititally Diary has not entries
"""
def test_inititially_diary_has_no_entries():
    diary = Diary()
    diary.all() == []
