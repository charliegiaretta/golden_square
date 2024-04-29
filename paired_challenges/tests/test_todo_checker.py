from lib.todo_checker import *

"""
If empty string given
Returns False
"""
def test_if_empty_string_given():
    result = check_if_todo("")
    assert result == False

"""
If string given without #TODO
Returns False
"""
def test_if_string_without_todo():
    result = check_if_todo("Hello")
    assert result == False

"""
If string does contain #TODO
Returns True
"""
def test_if_string_contains_todo():
    result = check_if_todo("Hello #TODO")
    assert result == True

"""
If string has no spaces but contains #TODO
Returns True
"""
def test_if_string_with_no_spaces_contains_todo():
    result = check_if_todo("Hello#TODOhello")
    assert result == True

"""
If string contains partially entered #TODO
Returns False
"""
def test_if_todo_is_partially_entered():
    result = check_if_todo("Hello TODO")
    assert result == False