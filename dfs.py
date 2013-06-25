# Depth-First Search
import helper
import sys

def depth_first(graph):
  """ Implements a depth-first search """
  searched_file = open('searched.txt', 'w')
  path_file = open('path.txt', 'w')
  
  stack = []
  visited = set()
  path = []
  
  root = 0
  goal = len(graph) - 1
  
  stack.append(root)
  visited.add(root)
  searched_file.write(str(root) + '\n')
  
  while stack:
    parent = stack.pop()
    path.append(parent)
    path_file.write(str(parent) + '\n')
    if parent == goal: break
    
    children = graph.neighbors(parent)
    for child in sorted(children):
      if child not in visited:
        searched_file.write(str(child) + '\n')
        visited.add(child)
        stack.append(child)  

if __name__ == "__main__":
  if len(sys.argv) is not 2:
    print "Invalid number of arguments."
    print "Proper Usage: python dfs.py <path_of_matrix_file>"
  else:
    cost_matrix = sys.argv[1]
    graph = helper.get_graph(cost_matrix)
    depth_first(graph)
  
  
  
  