import pytest
from lib.age_checker import *

"""
When date is given 
If user is under the age of 16
Return access denied message
"""

def test_access_denied_if_user_is_underage():
    result = age_checker('2010/01/01')
    assert result == 'Access denied!'

"""
When date is given 
If user is over the age of 16
Return access granted message
"""

def test_access_denied_if_user_is_correct_age():
    result = age_checker('1960/01/01')
    assert result == 'Access granted!'

"""
When no date is given
Raise exception and return error message that date is in incorrect format
"""

def test_access_raise_exception_when_no_date_given():
    with pytest.raises(Exception) as e:
        result = age_checker('')
    error_message = str(e.value)
    assert error_message == "Date is in incorrect format! Please use YYYY-MM-DD"