import helper
import sys
from collections import deque

def breadth_first(graph):
  """ Implements a breadth-first search """
  searched_file = open('searched.txt', 'w')
  path_file = open('path.txt', 'w')
  
  # I am implementing the frontier as a deque (double ended queue) 
  # so I can efficiently pop nodes at the beginning of the list. 
  frontier = deque()
  visited = set()
  
  root = 0
  goal = len(graph) - 1
  
  frontier.append(root)
  visited.add(root)
  
  # This will store the parent for each node that is explored
  path_dict = {}
  path_dict[root] = None
  
  while frontier:
    parent = frontier.popleft()
    searched_file.write(str(parent) + '\n')
    if parent == goal: break
    
    children = graph.neighbors(parent)
    for child in sorted(children):
      if child not in visited:
        visited.add(child)
        frontier.append(child)
        path_dict[child] = parent
        
  # Now, I will backtrace through the path_dict to get the path
  node = goal
  path = []
  while node is not None:
    path.insert(0, node)
    node = path_dict[node]
      
  for node in path:
    path_file.write(str(node) + '\n')
    
if __name__ == "__main__":
  if len(sys.argv) is not 2:
    print "Invalid number of arguments."
    print "Proper Usage: python bfs.py <path_of_matrix_file>"
  else:
    cost_matrix = sys.argv[1]
    graph = helper.get_graph(cost_matrix)
    breadth_first(graph)