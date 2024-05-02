from lib.track import Track 

"""
When we create a new track
We can get title and artist back
"""
def test_construct_track_and_get_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"

"""
When new track created
Formats track and artist
"""
def test_formats_title_and_artists():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"

