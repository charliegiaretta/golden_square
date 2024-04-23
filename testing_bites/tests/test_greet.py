from lib.greet import *

def test_greeter():
    result = greet('Charlie')
    assert result == "Hello, Charlie!"