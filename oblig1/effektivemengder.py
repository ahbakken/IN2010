#Effektive mengder, oblig1
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename
from this import s

#Lager noder for treet
class Node:
  def __init__(self, value, height):
    self.val = value
    self.left = None
    self.right = None
    self.height = height
    
# setter x inn i binaertreet or returnerer noden med x
# antar at treet er balansert og som gir: O(log(n))
def insert(root, x, h):
    if root.val == None:
        root = Node(x, h)
    elif (root.val < x):
        root.right = insert(root.right, x, h+1)
    else:
        root.left = insert(root.left, x, h+1)
    #Update size()
    return root

# sjekker om x er i treet 
# har samme kompleksitet som insert: O(log(n))
def contains(root, x):
    if root.val == None:
        return None
    if root.val == x:
        return root
    if x < root.val:
        return contains(root.left, x)
    if x > root.val:
        return contains(root.right, x)

def remove(root, x):
    #find the root and remove
    #return the root removed
    return root

#lager tom rotnode, uten innhold, hoyde -1
root = Node(None, -1)
print(root.val, root.height)
root = insert(root, 3, 0)
print(root.val, root.height)

# opner fil som stdin
filename = input("Enter filname: ")
f = open(filename, 'r')
i = int(f.readline())
x = 0
liste = (root)


# itererer gjennom fil for aa utfore oppgaver.
while x < i:
    line = f.readline()
    if line.startswith("insert"):
        tall = line.split(' ')
        verdi = int(tall[-1])
    # setter inn roten forst
        if (root.val == None): 
            root.val = verdi
            root.height = 0
    #om root har en verdi vil insert brukes
        else:
            liste.append(insert(root, verdi, 0))

    if line.startswith("contains"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        if contains(root, verdi):
            print("true")
        else: print("false")
    if line.startswith("remove"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        liste.remove(remove(root, verdi))
    if line.startswith("size"):
        print(len(liste))
f.close()
