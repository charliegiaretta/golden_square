from lib.task import Task
from lib.task_list import TaskList

"""
Task constructs with a title
"""
def test_task_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

"""
Newly constructed tasks are not complete
"""
def test_task_constructs_incomplete_tasks():
    task = Task("Walk the dog")
    assert task.complete == False

"""
When I mark task as complete
It is reflected in the complete property
"""
def test_marks_tasks_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.complete == True