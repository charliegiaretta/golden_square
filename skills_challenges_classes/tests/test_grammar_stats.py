from lib.grammar_stats import *

"""
When string is given
Return True if string begins with capital letter and ends with punctuation mark
"""
def test_if_string_begins_with_capital_letter_and_ends_with_punctuation_mark():
    grammarstats = GrammarStats()
    result = grammarstats.check('Hello.')
    assert result == True

"""
When string is given
Return False if string doesn't with capital letter and doesn't end with punctuation mark
"""
def test_if_string_does_not_begin_with_capital_letter_or_end_with_punctuation_mark():
    grammarstats = GrammarStats()
    result = grammarstats.check('hello')
    assert result == False

"""
When string is given
Return False if string doesn't with capital letter and but does end with punctuation mark
"""
def test_if_string_does_not_begin_with_capital_letter_but_does_end_with_punctuation_mark():
    grammarstats = GrammarStats()
    result = grammarstats.check('hello.')
    assert result == False

"""
When 4 texts are checked and 1 passes
Return percentage of texts which passed
"""
def test_to_check_percentage_of_passed_texts():
    grammarstats = GrammarStats()
    grammarstats.check('Hello.')
    grammarstats.check('hello.')
    grammarstats.check('hello')
    grammarstats.check('Hello')
    result = grammarstats.percentage_good()
    assert result == 25

"""
When 8 texts are checked and 4 passes
Return percentage of texts which passed
"""
def test_to_check_percentage_of_passed_texts():
    grammarstats = GrammarStats()
    grammarstats.check('Hello.')
    grammarstats.check('Hello.')
    grammarstats.check('Hello.')
    grammarstats.check('Hello.')
    grammarstats.check('Hello')
    grammarstats.check('hello.')
    grammarstats.check('hello')
    grammarstats.check('Hello')
    result = grammarstats.percentage_good()
    assert result == 50