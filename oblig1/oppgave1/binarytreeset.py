#Effektive mengder, oblig1
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

import fileinput

#Lager noder for treet
class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None
    self.size = 0

    
# setter x inn i binaertreet or returnerer noden med x
# antar at treet er balansert ved insert, som gir: O(log(n))
def insert(root, x):
    if root is None:
        return Node(x)
    elif (x < root.val):
        root.left = insert(root.left, x)  
    elif (x > root.val):
        root.right = insert(root.right, x)
    return root

# sjekker om x er i treet 
# har samme kompleksitet som insert: O(log(n))
def contains(root, x):
    if root is None:
        return False
    if root.val == x:
        return True
    if x < root.val:
        return contains(root.left, x)

    return contains(root.right, x)

#fjerner en node fra treet basert paa verdien som blir sendt inn. 
def remove(root, x):
    if root is None: 
        return root
    #om x er minde en rotverdien
    #fortsetter i venstre subtre
    if x < root.val:
        root.left = remove(root.left, x)
        return root
    #om x er storre en rotverdien
    #fortsetter i hoyre subtre
    elif x > root.val:
        root.right = remove(root.right, x)
        return root
    #if the root is a leaf node we make it None
    if root.left is None and root.right is None:
          return None
    #x er verken storre eller mindre, maa vaere lik rotverdien
    
    #sjekker om rot har barn venstre
    if root.left is None:
        temp = root.right #midlertidig holder for barnenoden
        root = None #dette er noden vi vil ha slettet
        return root #kobler sammen barn of bestemor til root-barn
    elif root.right is None:
        temp = root.left
        root = None
        return temp #barn returneres og tar plass til forelder
    #har to barn
    tempParent = root
    temp = root.right

    while temp.left != None:
        tempParent = temp
        temp = temp.left
    
    if tempParent != root:
        tempParent.left = temp.right
    else:
        tempParent.right = temp.right

    root.val = temp.val
    # print(root.val)
    return root

def size(root, x):
    while root != None:
        print(size)
        x += 1
        if root.left != None:
            size(root.left, x)
        if root.right != None:
            size(self.right)
    return x

#lager tom rotnode, uten innhold
root = None
sizeTree = 0

# opner fil som stdin
for line in fileinput.input():
    if line.startswith("insert"):
        tall = line.split(' ')
        verdi = int(tall[-1])
    # setter inn roten forst
        if (root == None): 
            root = insert(root, verdi)
            sizeTree+=1
            
    #om root har en verdi vil insert brukes
        else:
            if not contains(root,verdi):
                root = insert(root, verdi)
                sizeTree+=1
    elif line.startswith("contains"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        if contains(root, verdi):
            print("true")
        else: print("false")
    elif line.startswith("remove"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        if contains(root, verdi):
            root = remove(root, verdi) 
            sizeTree-=1
            
    #siden storrelsen paa treet blir oppdatert for hver remove og inser, vil 
    elif line.startswith("size"):
        print(sizeTree)

# itererer gjennom fil for aa utfore oppgaver.
