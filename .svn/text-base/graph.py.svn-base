class Graph:
  """
  The Graph will be a dictionary whose keys are the nodes of the graph.
  The value of each key will be a list of node tuples that are adjacent to the 
  key node.
  Example: Graph with one edge (1,2) of weight 3.
  G[1] = [(2, 3)]
  G[2] = [(1, 3)]
  """
  def __init__(self):
    """ Constructs an empty Graph object """
    self.G = {}
    
  def add_edge(self, node_i, node_j, weight=0):
    """ Adds weighted edge (node_i, node_j)."""
    if node_i in self.G.keys():
      self.G[node_i].append((node_j, weight))
    else:
      self.G[node_i] = [(node_j, weight)]
    if node_j in self.G.keys():
      self.G[node_j].append((node_i, weight))
    else:
      self.G[node_j] = [(node_i, weight)]
      
      
  def neighbors(self, node):
    """ Gets neighbors of node """
    if node in self.G.keys():
      return [neighbor for (neighbor, weight) in self.G[node]]
    else:
      return None
      
  def get_weight_of_edge(self, node_i, node_j):
    """ Returns the weight of edge (node_i, node_j) if edge exists.
    Otherwise, return None.
    """
    neighbor_nodes = self.G[node_i]
    if node_j in self.neighbors(node_i):
      # Assumes only one weight will be in list
      weight = [weight for (node, weight) in neighbor_nodes if node == node_j].pop()
      return weight
    else:
      return None
      
  def __len__(self):
    return len(self.G)
  
  def __str__(self):
    return str(self.G)

def tester():
  """ Small test unit for graph module """
  g = Graph()
  g.add_edge(1, 2, 5)
  g.add_edge(2, 3, 9)
  g.add_edge(3, 1, 4)
  
  assert g.neighbors(1) == [2, 3]
  assert g.neighbors(3) == [2, 1]
  assert g.neighbors(4) == None
  
  assert g.get_weight_of_edge(1, 2) == 5
  assert g.get_weight_of_edge(3, 1) == 4
  assert g.get_weight_of_edge(1, 3) == 4
  assert g.get_weight_of_edge(1, 4) == None
  
      
      
  
    
  
  