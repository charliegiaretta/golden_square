import pytest
from lib.password_checker import *

def test_password_checker_for_valid_password():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check('12345678') == True

def test_password_checker_for_invalid_password():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check('1234567')
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."
