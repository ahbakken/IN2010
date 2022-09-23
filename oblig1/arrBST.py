#sortert array til balansert soketre-liste
import sys
from typing import Optional, List

def arrToBST(array:list):
    if len(array) < 2:
        return array
    
    mid = len(array)//2

    left = arrToBST(array[:mid])
    right = arrToBST(array[mid+1:])

    return [array[mid]] + right + left


lines = sys.stdin.readlines()
input_list: List[Optional[int]] = [int(i) for i in lines]

output_list = arrToBST(input_list)

for i in output_list:
    print(i)