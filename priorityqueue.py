# Prioirty Queue module
# Source: Python Documentation
# I grabbed a lot of this code from the Python Documentation, but modified
# it to give priority to lower-numbered tasks. 
import heapq
import itertools

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, task, count]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, task, count = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return (task, priority)
    raise KeyError('pop from an empty priority queue')
    
def get_tasks():
  return [task for [priority, task, count] in pq]
  
def get_priority(task):
  return entry_finder[task][0]
    


