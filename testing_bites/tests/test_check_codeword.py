from lib.check_codeword import *

def test_codeword_is_correct():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_codeword_is_almost_correct():
    result = check_codeword('hose')
    assert result == "Close, but nope."

def test_codeword_is_wrong():
    result = check_codeword('sheep')
    assert result == "WRONG!"