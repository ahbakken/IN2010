#Effektive mengder, oblig1
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename

#Lager noder for treet
class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

    
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
    if root.val is x:
        return True
    if x < root.val:
        return contains(root.left, x)
    if x > root.val:
        return contains(root.right, x)

#hjelpeprosedyre, finner minste verdi i root
#skal finnes lengst til venstre i treet. 
def findMin(root):
    if root.left is not None:
        return findMin(root.left)
    else: 
        return root

#fjerner en node fra treet basert paa verdien som blir sendt inn. 
def remove(root, x):
    
    if root is None: 
        return root
    #om x er minde en rotverdien
    #fortsetter i venstre subtre
    if x < root.val:
        root.left = remove(root.left, x)
    #om x er storre en rotverdien
    #fortsetter i hoyre subtre
    elif x > root.val:
        root.right = remove(root.right, x)
    #x er verken storre eller mindre, maa vaere lik rotverdien
    else: 
        #sjekker om rot har barn venstre
        if root.left is None:
            temp = root.right #midlertidig holder for barnenoden
            root = temp #dette er noden vi vil ha slettet
            return root #kobler sammen barn of bestemor til root-barn
        elif root.right is None:
            temp = root.left
            root = temp
            #erstatte temp paa en anen maate
            return root #barn returneres og tar plass til forelder
        #har to barn
        temp = findMin(root.right)
        root.val = temp.val
        root.right = remove(root.right, temp.val)
        print(root.val)
    return root


#lager tom rotnode, uten innhold
root = None
sizeTree = 0

# opner fil som stdin
filename = input("Enter filname: ")
f = open(filename, 'r')
i = int(f.readline())
x = 0

# itererer gjennom fil for aa utfore oppgaver.
while x < i:
    line = f.readline()
    if line.startswith("insert"):
        tall = line.split(' ')
        verdi = int(tall[-1])
    # setter inn roten forst
        if (root == None): 
           root = insert(root, verdi)
    #om root har en verdi vil insert brukes
        else:
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
    elif line.startswith("size"):
        print(sizeTree)
    x+=1
f.close()
