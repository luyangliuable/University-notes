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

def median_of_five(arr: list[int], lo: int, hi: int) -> int:

def median_of_medians(arr: list[int], lo: int, hi: int) -> int:
    if hi - lo < 5:
        return median_of_five(arr, lo, hi)

def quicksort(arr) -> None:
    start = 0
    end = len(arr) - 1
    quicksort_aux(arr, start, end)


def quick_select(arr: list[int], k: int, hi: int, lo: int) -> int:
    if hi > lo:
        mid = partition(arr[lo: hi],  lo, hi)
        if k < mid:
            return quick_select(arr, k, lo, mid -1,)
        if k > mid:
            return quick_select(arr, k, lo, mid )
        else:
            return arr[k]
    else:
        return arr[k]


def quicksort_aux(arr, start: int, end: int):
    if start < end:
        boundary = partition( arr, start, end )
        quicksort_aux(arr, start, boundary-1)
        quicksort_aux(arr, boundary+1, end)
    else:
        return arr

arr = [i for i in range(1,10)]
print(quick_select(arr, 7, 0, len(arr) - 1))


