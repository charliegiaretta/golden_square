from lib.todo_list import *
from lib.todo import *

"""
When adding two instances of todo
We add them to the imcomplete list and return that list
"""
def test_create_two_todo_instances_and_add_to_incomplete_list():
    todolist = TodoList()
    todo_1 = Todo("Wash the dishes")
    todo_2 = Todo("Take out bins")
    todolist.add(todo_1)
    todolist.add(todo_2)
    assert todolist.incomplete() == [todo_1, todo_2]

"""
When adding two instances of todo
And marking them as complete
We return list of completed tasks
"""
def test_when_marked_complete_todo_tasks_included_in_completed_list():
    todolist = TodoList()
    todo_1 = Todo("Wash the dishes")
    todo_2 = Todo("Take out bins")
    todolist.add(todo_1)
    todolist.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todolist.complete() == [todo_1, todo_2]

"""
When adding two instances of todo
And using give_up to mark all todo tasks as complete
Returns all tasks in completed task list
"""
def test_when_marked_incomplete_and_give_up_is_used_all_tasks_marked_complete():
    todolist = TodoList()
    todo_1 = Todo("Wash the dishes")
    todo_2 = Todo("Take out bins")
    todolist.add(todo_1)
    todolist.add(todo_2)
    todolist.give_up()
    assert todolist.complete() == [todo_1, todo_2]