#bubble sort
#input: array with n elements
#output: sortet array with the same n elements
def bubbleSort(array):
    n = len(array)
    i = 0
    while (i < n-1):
        j = 0
        while (j < n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j+=1
        i+= 1
    return array

inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]

bubbleSort(inputList)
print(bubbleSort(inputList))