from lib.counter import *

def test_count_to_five():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."

def test_count_to_ten():
    count = Counter()
    count.add(10)
    result = count.report()
    assert result == "Counted to 10 so far."