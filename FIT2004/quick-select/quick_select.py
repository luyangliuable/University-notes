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

def partition(arr: list[int], start: int, end: int) -> int:
    mid =  (start + end) // 2
    pivot = arr[mid]

    arr[start], arr[mid] = arr[mid], arr[start]

    boundary = start

    for k in range(start + 1, end + 1):
        if arr[k] < pivot:
            arr[k], arr[boundary+1] = arr[boundary+1], arr[k]
            boundary += 1

    arr[start], arr[boundary] = arr[boundary], arr[start]

    print(arr)

    return boundary

arr = [i for i in range(0,10)]
value = 9
lo = 0
hi = len(arr) - 1
print("trying to find the", str( value + 1 ) + "th", "smalest value")
print(quick_select(arr, value, 0, len(arr) - 1))
