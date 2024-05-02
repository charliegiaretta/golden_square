from lib. diary_entry import DiaryEntry

"""
When I initialise with title and contents
I can get the title and contetns back
"""
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

"""
When I inititalise with a five word contents
Then #count_words should return five
"""
def test_count_words_should_returns_word_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three")
    assert diary_entry.count_words() == 3

"""
When I initialise with five word content
then reading_time with a wpm of 2 should return 3
"""
def test_reading_time():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_time(2) == 3