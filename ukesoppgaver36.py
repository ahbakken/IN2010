#Implement  algorithms from week 35
#depth of a node

class Node:
  def __init__(self, element):
    self.element = element
    self.leftChild = None
    self.rightChild = None
    self.parent = None
    
# algorithm for inserting new nodes to the binary tree
  def set_next_node(self, element):
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
    
#   def get_next_node(self):
#     return self.child
  
  def get_value(self):
    return self.element


root = Node(1)
root.set_next_node(2)
root.set_next_node(3)
root.set_next_node(4)
root.set_next_node(5)
root.set_next_node(6)

print(root.rightChild.element)

# # Algorithm to find depth of a given node
# def depth(self):
#     if self == None:
#         return -1
#     return 1+depth(self.parent)

# print('Depth e1:', depth(root))

# # Algorithm to find height of a given node
# def height(self):
#     h = -1
#     if self==None:
#         return h
#     for i in self.child:
#         h = max(h, height(i))
#     return 1+h

# print('Height e1:', height(root))

# # preorder traversing
# def preorder(self):
#     print("Preorder element:", self.element)
#     for i in self.child:
#         preorder(i)

# preorder(root)

# # postorder traversing
# def postorder(self):
#     for i in self.child:
#         postorder(i)
#     print('Postorder element:', self.element)

# postorder(root)