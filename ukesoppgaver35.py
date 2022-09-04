def BinarySearchIterative(liste, x):
    low = 0
    high = len(liste)-1
    while (low <= high): 
        i = int((low+high)/2)
        if (liste[i] == x): 
            return True
        elif (liste[i]<x):
            low = i+1
        elif (liste[i]>x):
            high = i-1
    return False

def SearchRecursive(liste, x, index):
    if (index<len(liste) and liste[index]==x):
        return True
    elif (index<len(liste)):
        return SearchRecursive(liste, x, index+1)
    else: return False

def BinarySearchRecursive(liste,x):
    index = int((len(liste)-1)/2)
    if index<len(liste):
        if (liste[index]==x):
            return True
        elif (liste[index]<x):
            return BinarySearchRecursive(liste[index+1:],x)
        elif (liste[index]>x):
            return BinarySearchRecursive(liste[0:index], x)
    else: return False

lis = [1,3,4,5,7,8,15,66, 123, 234, 333, 456, 465]

print('Iterative ', BinarySearchIterative(lis, 333))
print('Recursive:', SearchRecursive(lis, 333, 0))
print('Recursive:', BinarySearchRecursive(lis, 333))