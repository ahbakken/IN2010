import sys
from heapq import heappop, heappush
from typing import Optional, List


def heap_bal(heap):
    if len(heap) == 1:
        print(heap)
    if len(heap) == 2:
        a = heappop(heap)
        print(heap)
        print(a)
    else:
        r = []
        l = []

        hLen = len(heap)

        for i in range(hLen//2):
            heappush(l, heappop(heap))

        sys.stdout.write(f"{heappop(heap)}\n")

        for _ in range(hLen//2 - 1 + hLen % 2):
            heappush(r, heappop(heap))

        heap_bal(l)
        heap_bal(r)

lines = sys.stdin.readlines()
input_list: List[Optional[int]] = [int(i) for i in lines]

heap = []
for line in input_list:
    heappush(heap, int(line))