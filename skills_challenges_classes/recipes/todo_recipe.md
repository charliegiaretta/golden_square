# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

* We want to keep add tasks to a list and see a list of tasks
* We want to be able to remove tasks from a list by marking them 'complete'

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TodoTracker:
    def __init__(self)
    #Parameters: None

    def add(self, task):
    # Parameters:
    #     name: string
    # Side Effects:
    #     Adds task to a list
    pass
    
    def list_tasks(self)
    # Parameters: None
    # Side Effects:
    #     Shows list of tasks
    pass

    def remove_task(self, task)
    # Parameters: 
    #     name: string
    # Side Effects:
    #     Marks task as complete and removes from list
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a blank task
Returns a blank list
"""
tasks = ToDoTracker()
tasks.add_task("")
assert tasks.list_tasks() # => ""

"""
Given a task
Returns added task
"""
tasks = ToDoTracker()
tasks.add_task("Walk the dog")
assert tasks.list_tasks() # => "To do: Walk the dog"

"""
Given multiple tasks
Returns list of tasks added
"""
tasks = ToDoTracker()
tasks.add_task("Walk the dog")
tasks.add_task("Go to shops")
assert tasks.list_tasks() # => "To do: Walk the dog, Go to shops"

"""
Given a task that has been added to list
Removes task from list and returns message '{TASK} has been removed'
"""
tasks = ToDoTracker()
tasks.add_task("Walk the dog")
tasks.add_task("Go to shops")
tasks.remove_task("Walk the dog")
assert tasks.list_tasks() # => "To do: Go to shops"

"""
Given multiple tasks that have been added to list
Removes tasks from list and returns message '{TASK} has been removed'
"""
tasks = ToDoTracker()
tasks.add_task("Walk the dog")
tasks.add_task("Go to shops")
tasks.add_task("Cook dinner")
tasks.remove_task("Walk the dog")
tasks.remove_task("Go to shops")
assert tasks.list_tasks() # => "To do: Cook dinner"
```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
