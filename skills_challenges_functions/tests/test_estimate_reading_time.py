import pytest
from lib.estimate_reading_time import *

"""
If given text with 200 words
It will return an estimate reading time of 1
"""
def test_with_200_words():
    text = " ".join(['word' for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0

def test_with_400_words():
    text = " ".join(['word' for i in range(0,400)])
    result = estimate_reading_time(text)
    assert result == 2.0

def test_with_300_words():
    text = " ".join(['word' for i in range(0,300)])
    result = estimate_reading_time(text)
    assert result == 1.5

def test_with_empty_words():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for empty text"