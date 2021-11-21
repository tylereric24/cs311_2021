import random
import string

RANDOM_NODE_NAMES = ["Kona", "Riley", "Nahla", "Otis", "Templeton", "Gilligan", "Swiss", "Cooper", "Murphy", "Bristol", "Brady", "Stitch", "Charlie", "Diesel",
"Benji", "Archie", "Chi"]

NODE_PER_LAYER = [4,3,2] 
class Node:
  def __init__(self):
    self.children = [] 
    self.weight = [] 
    self.name = ''.join([random.RANDOM_NODE_NAMES[random.randrange(len(RANDOM_NODE_NAMES)]))
    
  def make_children(self, current_layer_number, node_per_layer_map):
    
    if current_layer_number >= len(node_per_layer_map):
      return
   
    for i in range( node_per_layer_map[current_layer_number] ):
      self.children.append( Node() )
  
    self.children[0].make_children( current_layer_number + 1, node_per_layer_map )
   
    for i in range(1, len(self.children) ):
      self.children[i].children = self.children[0].children[:]

  def print_layers(self, current_layer_number, node_per_layer_map):
    indent = '    ' * current_layer_number
   
    if current_layer_number >= len(node_per_layer_map):
      print(f"{indent} {self.name}")
      return
   
    print(f"{indent} {self.name} is connected to:")
    for i in range(len(self.children) ):
      try:
        print(f"{indent} Weight of {self.weight[i]}")
      except:
        pass
     
      self.children[i].print_layers(current_layer_number + 1, node_per_layer_map)
    
    return

  def weights(self, current_layer_number, node_per_layer_map):
   
    if current_layer_number >= len(node_per_layer_map):
      return
  
    self.weight = [0,0] * len(self.children)
   
    for i in range( len(self.children) ):
      self.weight[i] = random.uniform(0, 1)
     
      self.children[i].weights(current_layer_number + 1, node_per_layer_map)

    return

new_node = Node()
new_node.make_children(0, NODE_PER_LAYER)
new_node.weights(0, NODE_PER_LAYER)
new_node.print_layers(0, NODE_PER_LAYER)
