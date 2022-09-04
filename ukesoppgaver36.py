#Implement  algorithms from week 35
#depth of a node

class Node:
  def __init__(self, element):
    self.element = element
    self.leftChild = None
    self.rightChild = None
    self.parent = None
    
# Inserting new nodes to the binary tree
  def set_next_node(self, element):
    # check if new node will go on right or left side
    if self.element> element:
        if self.leftChild == None:
            self.leftChild = Node(element)
        else:
            self.leftChild.set_next_node(element)
    elif self.element<element:
        if self.rightChild == None:
            self.rightChild = Node(element)
        else:
            self.rightChild.set_next_node(element)
    return self

# Find node with element value x
  def find_node_value(self, x):
    if self == None:
      return None
    elif self.element == x:
      return self
    elif x<self.element:
      if self.leftChild == None:
        return None
      return self.leftChild.find_node_value(x)
    elif x>self.element:
      if self.rightChild == None:
        return None
      return self.rightChild.find_node_value(x)

# find smallest element
  def find_min_element(self):
    if self == None:
      return self
    current = self
    while current.leftChild is not None:
      current = current.leftChild 
    return current
  


# delete from binary tree

# Initialize class, insert new nodes to the tree
root = Node(15)
root.set_next_node(2)
root.set_next_node(6)
root.set_next_node(23)
root.set_next_node(1)
root.set_next_node(12) 
root.set_next_node(-23)                            

print("Root element value: ", root.element)

print("Find node with value x: ", (root.find_node_value(144)))

print(root.find_min_element().element)