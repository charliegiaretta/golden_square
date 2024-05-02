# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class BirthdayTracker():

    def __init__(self):
        self.birthday_record = {}

    def add(self, name, date):
        # Parameters: 
        # name: string
        # date: string
        # Side effects:
        # Add name and date to a dictionary of birthdays

    def all(self):
        # Parameters: 
        # None
        # Side effects:
        # Returns list of key value pairas

    def update_name(self, old_name, new_name):
        # Parameters: 
        # name: string
        # date: string
        # Side effects:
        # Updating the key of the given name

    def update_birthday(self, name, date):
        # Parameters: 
        # name: string
        # date: string
        # Side effects:
        # Updating the key value pair given

    def upcoming_birthday(self):
        # Parameters: 
        # None
        # Side effects:
        # Returns list of upcoming birthday key value pairs within 30 days

    def upcoming_ages(self, name):
        # Parameters: 
        # name: string
        # Side effects:
        # Returns age of key value pair

    def card_sent(self, name)
        # Parameters: 
        # name: string
        # Side effects:
        # Add 'done' to key value pair

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
When no data given
Returns an empty dictionary
"""
def test_returns_empty_dictionary():
    birthday_tracker = BirthdayTracker()
    assert birthday_tracker.all() == {}

"""
When adding single name and birthday
Returns the name and birthday
"""
def test_returns_name_and_birthday():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add("Laura", "16/11/1992")
    assert birthday_tracker.all() == {"Laura" : "16/11/1992"}

"""
When adding multiple names and birthday
Returns all names and birthdays
"""
def test_returns_multiple_names_and_birthdays():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add("Laura", "16/11/1992")
    birthday_tracker.add("Charlie", "26/05/1994")
    assert birthday_tracker.all() == {"Laura" : "16/11/1992", "Charlie" : "26/05/1994"}

"""
When adding a name but not a birthday
Raises exception
"""
def test_return_error_if_name_not_provided():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add("Eddie", "")
    assert RAISE EXCEPTION HERE

"""
When adding a birthday but not a name
Raises exception
"""
def test_return_error_if_birthday_not_provided():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add("", "01/01/1990")
    assert RAISE EXCEPTION HERE

"""
When adding a name and birthday with incomplete date
Raises exception
"""
def test_return_error_if_birthday_partially_entered():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add("Eddie", "01/1990")
    assert RAISE EXCEPTION HERE
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
