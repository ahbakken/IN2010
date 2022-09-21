#Effektive mengder, oblig1
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename

#Lager noder for treet
class Node:
  def __init__(self, value, height):
    self.val = value
    self.left = None
    self.right = None
    self.height = height
    
# setter x inn i binaertreet or returnerer noden med x
# antar at treet er balansert ved insert, som gir: O(log(n))
def insert(root, x, h):
    if root == None or root.val == None:
        root = Node(x, h)
    elif (root.val < x):
        root.right = insert(root.right, x, h+1)
    else:
        root.left = insert(root.left, x, h+1)
    return root

# sjekker om x er i treet 
# har samme kompleksitet som insert: O(log(n))
def contains(root, x):
    if root == None or root.val == None:
        return False
    if root.val == x:
        return True
    if x < root.val:
        return contains(root.left, x)
    if x > root.val:
        return contains(root.right, x)

#hjelpeprosedyre, finner minste verdi i root
#skal finnes lengst til venstre i treet. 
def findMin(root):
    if root == None or root.val == None:
        return root
    if root.left != None:
        return findMin(root.left)
    else: return root

#fjerner en node fra treet basert paa verdien som blir sendt inn. 
def remove(root, x):
    if root == None or root.val == None:
        return None
    if x < root.val:
        root.left = remove(root.left, x)
        return root
    if x > root.val:
        root.right = remove(root.right, x)
        return root
    if root.left == None:
        return root.right
    if root.right == None:
        return root.right
    holder = findMin(root.right)
    root.val = holder.val
    root.right = remove(root.right, holder.val)
    return root

#lager tom rotnode, uten innhold, hoyde -1
root = None

# opner fil som stdin
filename = input("Enter filname: ")
f = open(filename, 'r')
i = int(f.readline())
x = 0
liste = [root]
#oppdateres for hver gang en ny node legges til eller trekkes fra 
sizeList = len(liste)

# itererer gjennom fil for aa utfore oppgaver.
while x < i:
    line = f.readline()
    if line.startswith("insert"):
        tall = line.split(' ')
        verdi = int(tall[-1])
    # setter inn roten forst
        if (root == None): 
            root = Node(verdi, 0)
    #om root har en verdi vil insert brukes
        else:
            if (not contains(root, verdi)):
                liste.append(insert(root, verdi, 0))
                sizeList = len(liste)
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
            rem = remove(root, verdi)
            if (rem != None):
                liste.remove(rem)
                sizeList = len(liste)
    elif line.startswith("size"):
        print(sizeList)
    x+=1
f.close()
