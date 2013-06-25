import helper
import priorityqueue as pq
import sys

def a_star(graph, heuristic):
  """ Performs an A* search of the graph.
  Input:
  graph -- a graph implemented with the Graph.py module
  
  Output:
  Writes to searched.txt and path.txt
  """
  searched_file = open('searched.txt', 'w')
  path_file = open('path.txt', 'w')
  
  visited = set()
  
  root = 0
  goal = len(graph) - 1
  
  pq.add_task(root, 0)
  visited.add(root)
  
  # Keeps track of parents to build the path
  # path_dict[child_node] = parent_node
  path_dict = {}
  path_dict[root] = None
  
  while pq.pq:
    # Get the minimum cost node
    (node, cost) = pq.pop_task()
    searched_file.write(str(node) + '\n')
 
    if node == goal: break
    
    visited.add(node)
    children = graph.neighbors(node) 
    
    for child in sorted(children):
      frontier = pq.get_tasks()
      if child not in visited:
        # Need to subtract the previous heuristic so we don't double-count
        new_cost = ((cost - heuristic[node][goal]) + graph.get_weight_of_edge(node, child)
                   + heuristic[child][goal])
        if child not in frontier:
          pq.add_task(child, new_cost)
          path_dict[child] = node
        else:
          # Need to find the child in the frontier and replace
          old_cost = pq.get_priority(child)
          if old_cost > new_cost:
            pq.remove_task(child)
            pq.add_task(child, new_cost)
            path_dict[child] = node
  
  # Now, I will backtrace through the path_dict to get the path
  node = goal
  path = []
  while node is not None:
    path.insert(0, node)
    node = path_dict[node]

  for node in path:
    path_file.write(str(node) + '\n')
          
if __name__ == "__main__":
  if len(sys.argv) is not 3:
    print "Invalid number of arguments."
    print "Proper Usage: python astar.py <path_of_cost_matrix> <path_of_heuristic_matrix>"
  else:
    cost_matrix = sys.argv[1]
    heuristic_matrix = sys.argv[2]
    graph = helper.get_graph(cost_matrix)
    heuristic = helper.get_heuristic_array(heuristic_matrix)
    a_star(graph, heuristic)  