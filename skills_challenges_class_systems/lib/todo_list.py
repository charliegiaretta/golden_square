# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todo_list = []

    def add(self, todo):
        self._todo_list.append(todo)

    def incomplete(self):
        return [todo for todo in self._todo_list if not todo.complete]
    
    def complete(self):
        return [todo for todo in self._todo_list if todo.complete]

    def give_up(self):
        for todo in self._todo_list:
            todo.mark_complete()
