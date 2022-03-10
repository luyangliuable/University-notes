from heap import Heap
from random import randint

arr = [randint(1,25) for i in range(10)]
print(arr)

heap = Heap(len(arr))


for i in range(len(arr)):
    heap.add(arr[i])



