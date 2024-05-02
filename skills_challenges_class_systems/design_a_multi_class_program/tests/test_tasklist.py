from lib.task_list import TaskList

"""
Inititially TaskList has no incomplete tasks
"""
def test_tasklist_initialises_with_no_tasks():
    task_list = TaskList()
    assert task_list.all_incomplete() == []