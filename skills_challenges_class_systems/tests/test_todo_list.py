from lib.todo_list import *

"""
When initialised have been added
Returns blank incomplete todo list
"""
def test_when_initialised_todo_incomplete_list_is_blank():
    todolist = TodoList()
    assert todolist.incomplete() == []

"""
When initialised and no tasks have been added
Returns blank complete todo list
"""
def test_when_initialised_todo_complete_list_is_blank():
    todolist = TodoList()
    assert todolist.complete() == []

