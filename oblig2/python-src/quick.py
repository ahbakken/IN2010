#quick.py
import random
from countcompares import CountCompares
from countswaps import CountSwaps

#quicksort runtime, worst case is O(n^2)
#but happens rarely

def sort(A):
    low = 0
    high = len(A) - 1
    quickSort(A, low, high)
    return A

def partition(A, low, high):
    p = random.randint(low, high)
    A.swap(p, high)
    pivot = A[high]
    left = low
    right = high - 1
    while left <= right:
        # print(A)
        while left <= right and A[left] <= pivot:
            left+=1
        while right >= left and A[right] >= pivot:
            right-=1
        if left < right:
            A.swap(left, right)

    A.swap(left, high)
    return left

def quickSort(A, low, high):
    if low >= high:
        return A
    p = partition(A, low, high)
    quickSort(A, low, p-1)
    quickSort(A, p+1, high)
    return A

# TEST
# inputList = [80, 91, 7, 33, 50, 70, 13, 321, 12]
# countA = CountSwaps([CountCompares(x) for x in inputList])
# print(sort(countA))