# ineffektiveMengder.py
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename
import string

#Sjekker om x er i mengden og returnerer True om den er det
def contains(mengden, x):
    check = False
    for i in mengden:
        if i == x:
            check = True
    return check


# setter x inn i mengden (uten duplikater, ved aa bruke contains)
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

# itererer gjennom fil for aa utfore oppgaver.
while x < i:
    line = f.readline()
    if line.startswith("insert"):
        verdi = int(line[-2])
        mengde = (insert(mengde, verdi))
    if line.startswith("contains"):
        verdi = int(line[-2])
        print(contains(mengde, verdi))
    if line.startswith("remove"):
        verdi = int(line[-2])
        mengde = remove(mengde, verdi)
    if line.startswith("size"):
        print(size(mengde))
    x+=1
f.close()