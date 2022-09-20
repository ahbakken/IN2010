# ineffektiveMengder.py
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename

#Sjekker om x er i mengden og returnerer True om den er det
def contains(mengden, x):
    check = False
    for i in mengden:
        if i == x:
            check = True
    return check

# setter x inn i binaertreet
def insert(mengden, x):
    if(contains(mengden, x)):
        return mengden
    else:
        mengden.add(x)
        return mengden

# fjerner x fra mengden
def remove(mengden, x):
    newSet = set()
    for i in mengden:
        if i != x:
            newSet.add(i)
    return newSet

# gir antall elementer i mengden
def size(mengden):
    counter = 0
    for i in mengden:
        counter+=1
    return counter

# opner fil som stdin
filename = input("Enter filname: ")
f = open(filename, 'r')
i = int(f.readline())
x = 0
mengde = set()

# lag mengde først, så iterer gjennom denne og insert
# dette vil forhindre 
# itererer gjennom fil for aa utfore oppgaver.
while x < i:
    line = f.readline()
    if line.startswith("insert"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        mengde = (insert(mengde, verdi))
    if line.startswith("contains"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        if contains(mengde, verdi):
            print("true")
        else: print("false")
    if line.startswith("remove"):
        tall = line.split(' ')
        verdi = int(tall[-1])
        mengde = remove(mengde, verdi)
    if line.startswith("size"):
        print(size(mengde))
    x+=1
    # print(mengde)
f.close()