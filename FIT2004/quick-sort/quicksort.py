# Hoare Partition algorithm
import time
from collections import defaultdict
from random import randint

def partition(arr: list[int], start: int, end: int) -> int:
    print("start of partition is", start, "end of partition is", end)
    mid =  (start + end) // 2
    print("mid is", arr[mid], "at position", mid)
    pivot = arr[mid]

    arr[start], arr[mid] = arr[mid], arr[start]

    boundary = start

    for k in range(start + 1, end + 1):
        print("for k:", k, "and array", arr)
        print("boundary:", boundary)
        if arr[k] < pivot:
            arr[k], arr[boundary+1] = arr[boundary+1], arr[k]
            boundary += 1

    arr[start], arr[boundary] = arr[boundary], arr[start]

    print(arr)

    return boundary

def quicksort(arr) -> None:
    start = 0
    end = len(arr) - 1
    quicksort_aux(arr, start, end)


def quicksort_aux(arr, start: int, end: int):
    if start < end:
        boundary = partition( arr, start, end )
        quicksort_aux(arr, start, boundary-1)
        quicksort_aux(arr, boundary+1, end)
    else:
        return arr

arr = [randint(1,99) for _ in range(25)]
start_time = time.process_time()
quicksort(arr)
end_time = time.process_time() - start_time
cp = [0]*len(arr)
for i,item in enumerate(arr):
    cp[i] = item

print("original array unsorted was", cp)
print("the sorted array is", arr)
print("it took approx", str( end_time ) + "s", "to process this")

