# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```python
class Diary():
    def add(self, diary_entry):
        # diary_entry: instance of diary entry
        # returns nothing
        # side effects: adds to list of diary entries
        pass

    def all(self):
        # returns a list of all diary entries
        pass

class DiaryEntry():
    def __init__(self, title, contents):
        # title: a string representing title of diary entry
        # contents: a string representing content of diary entry
        # side effects: sets the above properties
        pass

class TaskList():
    def add(self, task):
        # instance of a task
        # returns nothing
        # side effects: adds to list of tasks
        pass

    def all_incomplete(self):
        # returns a list of instances of class
        # representing the incomplete tasks
        pass

    def all_complete(self):
        # returns a list of instances of class
        # representing the complete tasks
        pass

class Task():
    def __init__(self, title):
        # title: a string representing a job to do
        # side effect: sets title property
        pass

    def mark_complete(self):
        # side effect: marks the task as complete
        # returns nothing
        pass

class PhoneNumberExtractor():
    def __init__(self, diary):
        # diary: an instance of Diary
        # side effect: sets diary property
        pass

    def extract(self):
        # returns a list of strings
        # representing phone numbers
        pass


class ReadableEntryFinder():
    def __init__(self, diary):
        # diary: an instance of Diary
        # side effect: sets diary property
        pass

    def extract(self, wpm, minutes):
        # wpm: integer
        # minutes: integer
        # returns the longest diary entry that can be read
        # in the given time given the wpm and minutes
        pass 
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python


"""
When I list multiple diary entries
#all lists them out in order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My Contents 1")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() # => [entry_1, entry_2, entry_3]

"""
When I list multiple tasks
and I mark one as complete
#all_complete shows the incomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Go to shops")
task_3 = Task("Take out bins")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() # => [task_1, task_2, task_3]


"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the incomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Go to shops")
task_3 = Task("Take out bins")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() # => [task_1, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the complete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Go to shops")
task_3 = Task("Take out bins")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_complete() # => [task_2]

"""
When I add multiple diary entires
And i call PhoneNumberExtractor #extract
I get a list of phone numbers from all diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000001")
entry_2 = DiaryEntry("My Title 2", "My friend is 07800000002")
entry_3 = DiaryEntry("My Title 3", "My contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["07800000000", "07800000001", "07800000002"]

"""
When I add multiple diary entires
And i call PhoneNumberExtractor #extract
It ignores duplicate numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000000")
entry_2 = DiaryEntry("My Title 2", "My friend is 07800000000")
entry_3 = DiaryEntry()
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["07800000000"]

"""
When I add multiple diary entires
And I call PhoneNumberExtractor #extract
It ignores non-valid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 0780000000000 and 0780000000")
entry_2 = DiaryEntry("My Title 1", "My friend is 07800 230002")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

"""
When I add no diary entires
And I call PhoneNumberExtractor #extract
It returns an empty list
"""
diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

"""
When I add one diary entry
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four")
diary.add(entry_1)
extractor = ReadibleEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_1

"""
When I add one diary entry that does not fit in the time
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns None
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
diary.add(entry_1)
extractor = ReadibleEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => None

"""
When I add multiple diary entries, one readable
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
entry_2 = DiaryEntry("My Title 1", "one two three four")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadibleEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_2

"""
When I add multiple diary entries, multiple readable
and I call ReadableEntryExtractor #extract
With a wpm of 2 and a minutes of 2
It returns the longest readable one
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
entry_2 = DiaryEntry("My Title 1", "one two three four")
entry_3 = DiaryEntry("My Title 1", "one two three")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadibleEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => entry_2

"""
When I add no diary entries
and I call ReadableEntryExtractor #extract
It returns None
"""
diary = Diary()
extractor = ReadibleEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) # => None

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE
# Diary
"""
Inititally Diary has not entries
"""
diary = Diary()
diary.all() # => []

# Diary Entry
"""
DiaryEntry is constructed with a Title and Contents
"""
entry = DiaryEntry("My Title", "My Contents")
entry.title # => "My Title"
entry.content # => "My Content"

# TaskList
"""
Inititially TaskList has no incomplete tasks
"""
task_list = TaskList()
task_list.all() # => []

"""
Inititially TaskList has no complete tasks
"""
task_list = TaskList()
task_list.all() # => []

#Task
"""
Task constructs with a title
"""
task = Task("Walk the dog")
task.title # => "Walk the dog"

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
