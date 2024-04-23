from lib.report_length import *

def test_report_length_hello():
    result = report_length('Hello')
    assert result == "This string was 5 characters long."

def test_report_length_goodbye():
    result = report_length('Goodbye')
    assert result == "This string was 7 characters long."

def test_report_length_nothing():
    result = report_length('')
    assert result == "This string was 0 characters long."