import random
import string

NODE_PER_LAYER = [4,3,2] #Global variable/list
#class holds data and methods self=this
class Node:
  def __init__(self):
    self.children = [] #connection to list of children
    self.weight = [] #list of weight of connection to children
    self.name = ''.join([random.choice(string.ascii_letters) for i in range(3)]) #set a random name to each Node

  def make_children(self, current_layer_number, node_per_layer_map):
    #base case
    if current_layer_number >= len(node_per_layer_map):
      return
    #create all children for this layer
    for i in range( node_per_layer_map[current_layer_number] ):
      self.children.append( Node() )
    #recursively connect children for next layers
    self.children[0].make_children( current_layer_number + 1, node_per_layer_map )
    #copy all children from [0] to all other chldren (deep copy)
    for i in range(1, len(self.children) ):
      self.children[i].children = self.children[0].children[:]

  def print_layers(self, current_layer_number, node_per_layer_map):
    indent = '    ' * current_layer_number #makes output look nice
    #base case
    if current_layer_number >= len(node_per_layer_map):
      print(f"{indent} {self.name}")
      return
    #so output makes sense
    print(f"{indent} {self.name} is connected to:")
    for i in range(len(self.children) ):
      try:
        print(f"{indent} Weight of {self.weight[i]}")
      except:
        pass
      #recurse
      self.children[i].print_layers(current_layer_number + 1, node_per_layer_map)
    
    return

  def weights(self, current_layer_number, node_per_layer_map):
    #base case
    if current_layer_number >= len(node_per_layer_map):
      return
    #initialize
    self.weight = [0,0] * len(self.children)
    #set random weights
    for i in range( len(self.children) ):
      self.weight[i] = random.uniform(0, 1)
      #recurse
      self.children[i].weights(current_layer_number + 1, node_per_layer_map)

    return
#master node
new_node = Node()
#create all the children
new_node.make_children(0, NODE_PER_LAYER)
#set all the weights
new_node.weights(0, NODE_PER_LAYER)
#output the results
new_node.print_layers(0, NODE_PER_LAYER)
