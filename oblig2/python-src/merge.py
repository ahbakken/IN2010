#split array in two, sort the two halfs, merge them together
# use merge sort recursive
# O(n log(n))
from countcompares import CountCompares
from countswaps import CountSwaps
import math

def sort(array):
    n = len(array)
    if n <= 1:
        return array
    i = int(math.floor((n/2)))
    a1 = sort(array[0:i])
    a2 = sort(array[i:n])
    return merge(a1, a2, array)

def merge(A1, A2, A):
    i = 0
    j = 0
    while i<len(A1) and j<len(A2):
        if A1[i] < A2[j]:
            A[j+i] = A1[i]
            i+=1
        else:
            A[j+i] = A2[j]
            j+=1
    while i<len(A1):
        A[j+i] = A1[i]
        i+=1
    while j<len(A2):
        A[j+i] = A2[j]
        j+=1
    return A


# # TEST
# inputList = [80, 91, 7, 33, 50, 70, 13, 321, 12]
# countA = CountSwaps([CountCompares(x) for x in inputList])
# print(sort(countA))