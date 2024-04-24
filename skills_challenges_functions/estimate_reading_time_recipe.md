# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature


_Include the name of the function, its parameters, return value, and side effects._
```python
def estimate_reading_time(text):
    # Paremeters:
    #   text: a string containing words
    # Return:
    #   A float representing estimated reading time
    # E.g. "2.0"
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
If given text with 200 words
It will return an estimate reading time of 1
"""
estimate reading time()
# => 1.0

"""
If given text with 400 words
It will return an estimate reading time of 2
"""
estimate reading time()
# => 2.0

"""
If given text with 300 words
It will return an estimate reading time of 1.5
"""
estimate reading time()
# => 1.5

"""
If given empty text
Returns error message
"""
estimate reading time()
# => Raises error "Can't estimate reading time for empty text"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
