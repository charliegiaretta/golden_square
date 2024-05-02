from lib.music_library import MusicLibrary

"""
Inititally
There are no tracks
"""
def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

"""
Inititally 
Searching for tracks gets an empty list
"""
def test_initially_searches_return_empty():
    library = MusicLibrary()
    assert library.search_by_title("") == []
