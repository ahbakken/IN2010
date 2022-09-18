#sorting
#input: array with n elements
#output: sortet array with the same n elements

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

inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
print("Before bubble sort", inputList)
print("After  bubble sort", bubbleSort(inputList))
print("__________________________________________________________")

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
        print(array)
    return array

inputList = [1, 5, 12, 34, 54, 42, 33, 65, 56, 555, 64, 13 ,47 , 0]
print("Before selection sort", inputList)
print("After  selection sort", selectionSort(inputList))
print("__________________________________________________________")

