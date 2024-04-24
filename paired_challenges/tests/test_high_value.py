from lib.high_value import *

def test_if_first_value_higher_works():
    highvalue = HighValue(value_first=10, value_second=5)
    assert highvalue.get_highest() == "First value is higher"

def test_if_second_value_higher_works():
    highvalue = HighValue(value_first=5, value_second=10)
    assert highvalue.get_highest() == "Second value is higher"

def test_if_values_are_equal():
    highvalue = HighValue(value_first=5, value_second=5)
    assert highvalue.get_highest() == "Values are equal"

def test_if_first_value_higher_works_after_adding():
    highvalue = HighValue(value_first=5, value_second=10)
    highvalue.add(10, 'first')
    assert highvalue.get_highest() == "First value is higher"

def test_if_second_value_higher_works_after_adding():
    highvalue = HighValue(value_first=10, value_second=5)
    highvalue.add(10, 'second')
    assert highvalue.get_highest() == "Second value is higher"

def test_if_both_values_are_equal_after_adding():
    highvalue = HighValue(value_first=10, value_second=5)
    highvalue.add(5, 'second')
    assert highvalue.get_highest() == "Values are equal"