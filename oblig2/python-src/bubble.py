#bubblesort
#runtime O(n^2)
from countcompares import CountCompares
from countswaps import CountSwaps

def sort(array):
    n = len(array)
    i = 0
    while (i < n-1): #stop at n-2
        j = 0
        while (j < n-i-1): #stop at n-2
            if array[j] > array[j+1]:
                array.swap(j, j+1)
            j+=1
        i+= 1
    return array

# TEST
# inputList = [80, 91, 7, 33, 50, 70, 13, 321, 12]
# countA = CountSwaps([CountCompares(x) for x in inputList])
# print(sort(countA))