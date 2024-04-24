from lib.personal_diary import *

"""
Returns empty string if empty string given
"""

def test_return_empty_string():
    result = make_snippet('')
    assert result == ''

"""
Returns string of four words if four words are given
"""

def test_return_four_words_if_four_words_given():
    result = make_snippet('one two three four')
    assert result == 'one two three four'

"""
Returns string of five words if five words are given
"""

def test_return_five_words_if_five_words_given():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'

"""
Returns first five words of string + ellipsis if string
has more than five words
"""

def test_return_shortened_string():
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five...'

"""
Returns number of words in string with three words
"""
def test_returns_number_of_words_in_string():
    result = count_words('one two three')
    assert result == 3