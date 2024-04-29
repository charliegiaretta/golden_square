from lib.todo_tracker import ToDoTracker

"""
Initially there are no tasks
"""
def test_initially_has_no_tasks():
    tasks = ToDoTracker()
    assert tasks.list_incomplete() == []

"""
Given a task
Returns added task
"""
def test_adding_a_task():
    tasks = ToDoTracker()
    tasks.add("Walk the dog")
    assert tasks.list_incomplete() == ["Walk the dog"]

"""
Given multiple tasks
Returns list of tasks added
"""
def test_adding_multiple_tasks():
    tasks = ToDoTracker()
    tasks.add("Walk the dog")
    tasks.add("Go to shops")
    assert tasks.list_incomplete() == ["Walk the dog", "Go to shops"]

"""
Given multiple tasks
And mark one as complete
It disappears from task list
"""
def test_removing_task():
    tasks = ToDoTracker()
    tasks.add("Walk the dog")
    tasks.add("Go to shops")
    tasks.mark_complete(0)
    assert tasks.list_incomplete() == ["Go to shops"]
