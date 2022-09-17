#Binary heaps implementation
#put in a list
import math

def parentOf(i):
    return int(math.floor((i-1)/2))

def leftOf(i):
    return int(math.floor(2*(i+1)))

def rightOf(i):
    return int(math.floor(2*(i+2)))

def insert(array, element):
    i = len(array) #length before append
    array.append(element) #appends to the end of the list
    while ((0 < i) and array[i] < array[parentOf(i)]):
        array[i], array[parentOf(i)] = array[parentOf(i)], array[i] #switch i and parent of i
        i = parentOf(i)

def removeMin(array):
    x = array[0]
    length = len(array)-1
    array[0] = array[length]
    i = 0
    while (rightOf(i) < length):
        j = 0
        if (array[leftOf(i)] <= array[rightOf(i)]):
            j = leftOf(i)
        else: j = rightOf(i)
        if (array[j] <= array[i]):
            array[i], array[j] = array[j], array[i]
            i = j
        else: break
    if (leftOf(i) < length and (array[leftOf(i)] <= array[i])):
        array[i], array[leftOf(i)] = array[leftOf(i)], array[i]
    array.pop()
    return x

inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
tree = []

print(tree)
insert(tree, 27)
print(tree) 
for i in inputList:
    insert(tree, i)

print(tree)
print(len(tree))

print(removeMin(tree))

print(tree)
print(len(tree))

