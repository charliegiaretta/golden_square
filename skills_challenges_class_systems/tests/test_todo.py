from lib.todo import *

"""
When initialised with task
Returns task back
"""
def test_when_initialised_todo_is_blank():
    todo = Todo("Wash the dishes")
    assert todo.task == "Wash the dishes"

"""
When initialised and task added
Returns incomplete (False) by default
"""
def test_when_task_initialised_return_incomplete():
    todo = Todo("Wash the dishes")
    assert todo.complete == False