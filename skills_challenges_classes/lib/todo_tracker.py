class ToDoTracker():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def list_incomplete(self):
        return self.tasks

    def mark_complete(self, index):
        del self.tasks[index]
    
    
    
    
    
    
    
    
    
    
    # def add_task(self, task):
    #     return self.tasks.append(task)
    
    # def list_tasks(self):
    #     tasks =  ', '.join(self.tasks)
    #     return f'To do: {tasks}'

    # def remove_task(self, task):
    #     return self.tasks.remove(task)