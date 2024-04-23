import pytest
from lib.present import *

def test_present_wrap_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_already_wrapped_present():
    present = Present()
    present.wrap(33)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_first_wrapped_value_preserved():
    present = Present()
    present.wrap(33)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    assert present.unwrap() == 33