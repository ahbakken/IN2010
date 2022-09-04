# ineffektiveMengder.py
# contains(set, x) er x med i mengden?
# insert(set, x) setter x inn i mengden (uten duplikater)
# remove(set, x) fjerner x fra mengden
# size(set) gir antall elementer i mengden

from fileinput import filename


mengden = {1, 3, 53 ,2 ,5,24}

#Sjekker om x er i mengden og returnerer True om den er det
def contains(mengden, x):
    check = False
    for i in mengden:
        if i == x:
            check = True
    return check

print(contains(mengden, 2))

# setter x inn i mengden (uten duplikater, ved aa bruke contains)
def insert(mengden, x):
    if(contains(mengden, x)):
        return mengden
    else:
        mengden.add(x)
        return mengden

print(insert(mengden, 153))

# fjerner x fra mengden
def remove(mengden, x):
    newSet = set()
    for i in mengden:
        if i != x:
            newSet.add(i)
    return newSet

print(remove(mengden, 153))

# gir antall elementer i mengden
def size(mengden):
    counter = 0
    for i in mengden:
        counter+=1
    return counter

print(size(mengden))

filename = input("Enter filname: ")
f = open(filename, 'r')






f.close()