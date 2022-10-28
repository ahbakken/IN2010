#insertion.py
from countcompares import CountCompares
from countswaps import CountSwaps
    
def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]

def sort(A):
    n = len(A)
    i = 1
    while (i < n): #iterate throught the array, stop after n-1
        j = i
        while (j > 0 and A[j-1] > A[j]):
            A.swap(j, j-1)
            j = j-1
            #print(array)
        i+=1

    return A


# inputList = [80, 91, 7, 33, 50, 70, 13, 321, 12]
# countA = CountSwaps([CountCompares(x) for x in inputList])
# print("After  insertion sort", sort(countA))


