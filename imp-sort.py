#sorting
#input: array with n elements
#output: a sortet array with the same n elements

#bubble sort
def bubbleSort(array):
    n = len(array)
    i = 0
    while (i < n-1): #stop at n-2
        j = 0
        while (j < n-i-1): #stop at n-2
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j+=1
        i+= 1
    return array

# inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
# print("Before bubble sort", inputList)
# print("After  bubble sort", bubbleSort(inputList))
# print("__________________________________________________________")

#selection sort
def selectionSort(array):
    n = len(array)
    i = 0
    while (i < n-1): #iterate throught the array, stop after n-2
        k = i
        j = i+1
        while j < n:  #iterate through the array again, stop at n-1
            if array[j] < array[k]: #check if element after is bigger than element before
                k = j #change value of k to the smallest element in the array
            j+=1
        if i != k:  
            array[i], array[k] = array[k], array[i] #swap place for i and the smallest element after i
        i+=1
        #print(array)
    return array

# inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
# print("Before selection sort", inputList)
# print("After  selection sort", selectionSort(inputList))
# print("__________________________________________________________")

#insertion sort
def insertionSort(array):
    n = len(array)
    i = 1
    while (i < n): #iterate throught the array, stop after n-1
        j = i
        while (j > 0 and array[j-1] > array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j = j-1
            #print(array)
        i+=1
        
    return array

# inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
# print("Before insertion sort", inputList)
# print("After  insertion sort", insertionSort(inputList))
# print("__________________________________________________________")

#heapsort
#build max-heap, help procedure for heapsort
from logging import LoggerAdapter
import math
from turtle import left, right
def buildMaxHeap(array, n):
    i = int(math.floor(n/2))
    while i >= 0:
        bubbleDown(array, i, n)
        i-=1

#bubble down, help procedure for build max-heap
def bubbleDown(array, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and array[largest] < array[left]:
        largest, left = left, largest
    if right < n and array[largest] < array[right]:
        largest, right = right, largest
    if i != largest:
        array[i], array[largest] = array[largest], array[i]
        bubbleDown(array, largest, n)

#heapsort
def heapSort(array):
    buildMaxHeap(array, len(array))
    i = len(array)-1
    while i >= 0:
        array[0], array[i] = array[i], array[0]
        bubbleDown(array, i, len(array))
        i-=1
    return array


# inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
# print("Before heapsort sort", inputList)
# print("After  heapsort sort", heapSort(inputList))
# print("__________________________________________________________")

#mergesort
#split array in two, sort the two halfs, merge them together
# use merge sort recursive
# O(n log(n))
def mergesort(array):
    n = len(array)
    if n <= 1:
        return array
    i = int(math.floor((n/2)))
    a1 = mergesort(array[0:i])
    a2 = mergesort(array[i:n])
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

inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
print("Before mergesort", inputList)
print("After  mergesort", mergesort(inputList))
print("__________________________________________________________")


#quicksort
#moves elements that are smaller left, and bigger rigth than a given index

import random
def partition(A, low, high):
    # p = int(math.floor((len(A)/2)))
    p = random.randint(low, high)
    A[p], A[high] = A[high], A[p]
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
            A[left], A[right] = A[right], A[left]

    A[left], A[high] = A[high], A[left]
    return left

def quickSort(A, low, high):
    if low >= high:
        return A
    p = partition(A, low, high)
    quickSort(A, low, p-1)
    quickSort(A, p+1, high)
    return A

# inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
# print("Before quicksort sort", inputList)
# print("After  quicksort sort", quickSort(inputList, 0, (len(inputList)-1)))
# print("__________________________________________________________")

