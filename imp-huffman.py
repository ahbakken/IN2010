#Huffman coding
#use binary heaps for priority queue

from logging import root
import math

#make nodes, hold symbol and frequency
class Node:
  def __init__(self, symbol, frequency, leftChild, rightChild):
    self.sym = symbol
    self.freq = frequency
    self.left = leftChild
    self.right = rightChild
    self.parent = None
    
#find parents or children
def parentOf(i):
    return int(math.floor((i-1)/2))
def leftOf(i):
    return int(math.floor(2*(i+1)))
def rightOf(i):
    return int(math.floor(2*(i+2)))

#insert into the 
def insert(array, node):
    i = len(array) #length before append
    array.append(node) #appends to the end of the list
    while ((0 < i) and array[i].freq < array[parentOf(i)].freq): #while i is smaller than parent
        array[i], array[parentOf(i)] = array[parentOf(i)], array[i] #switch i and parent of i 
        i = parentOf(i)

def removeMin(array):
    x = array[0]
    length = len(array)-1
    array[0] = array[length]
    i = 0
    while (rightOf(i) < length):
        j = 0
        if (array[leftOf(i)].freq <= array[rightOf(i)].freq):
            j = leftOf(i)
        else: j = rightOf(i)
        if (array[j].freq <= array[i].freq):
            array[i], array[j] = array[j], array[i]
            i = j
        else: break
    if (leftOf(i) < length and (array[leftOf(i)].freq <= array[i].freq)):
        array[i], array[leftOf(i)] = array[leftOf(i)], array[i]
    array.pop()
    return x

def huffman(c):
    q = []
    for i in c:
        insert(q, Node(i[0], i[1], None, None))
        print(q[-1].sym, q[-1].freq)
    while len(q) > 1:
        v1 = removeMin(q)
        v2 = removeMin(q)
        f = v1.freq + v2.freq
        insert(q, Node(None, f, v1, v2))
    return removeMin(q)

list = (('a', 1), ('b', 5), ('i', 4), ('e', 23), ('y', 6), ('g', 1), (' ', 7))


root = huffman(list)
print('____________________________________________________________')
print(root.freq)

node = root
while (node.right != None):
    print(node.sym, node.freq)
    node = node.right

