# function SORT-AND-COUNTINV(array[lo..hi])
# iflo=hithen
# return (array[lo],0)
# else
# mid = ⌊(lo + hi)/2⌋
# (array[lo..mid],InvL ) = SORT-AND-COUNTINV(array[lo..mid])
# (array[mid+1..hi],InvH ) = SORT-AND-COUNTINV(array[mid+1..hi])
# (array[lo..hi], InvS ) = MERGE-AND-COUNTSPLITINV(array[lo..mid], array[mid + 1..hi])
# Inv=InvL +InvH +InvS
# return (array[lo..hi],Inv)

import random
import time

def sort_and_countinv(arr: list) -> tuple:
    if len(arr) == 1:
        return arr, 0

    else:
        mid = len(arr) // 2
        print("mid is", mid)
        L, invL = sort_and_countinv(arr[:mid])
        H, invH = sort_and_countinv(arr[mid:])
        S, invS = merge_and_count(arr[mid:], arr[:mid])
        inv = invL + invH + invS

        return arr, inv

# functionMERGE-AND-COUNTSPLITINV(A[i..n1],B[j..n2]) result = empty array
# splitInversions = 0
# whilei≤n1 orj≤n2 do
# if j >n2 or(i ≤n1 andA[i]≤B[j])then result.append(A[i ])
# i += 1
# else
# result.append(B[ j ])
# j += 1
# splitInversions = splitInversions + n1 - i + 1
# return (result, splitInversions)

def merge_and_count(A: list, B: list) -> tuple:
    result = []
    splitInversions = 0

    i = j = 0
    while i <= len(A)-1 or j <= len(B)-1:
        print(A[i])
        if j > len(B) or (i < len(A) and A[i] <= B[j]):
            result.append(A[i])
            i += 1

        else:
            result.append(B[j])
            j += 1

            splitInversions = splitInversions + len(A) - i + 1

    return result, splitInversions

arr = [25, 20, 16, 20, 6]
n = len(arr)
print("number of inversions are", sort_and_countinv(arr))
