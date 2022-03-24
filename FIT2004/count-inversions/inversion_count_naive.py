import time
import random
# Python3 program to count inversions
# in an array
def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                print(arr[i], arr[j])
                inv_count += 1

    return inv_count


arr = [25, 20, 16, 20, 6]
n = len(arr)
print("Number of inversions are", getInvCount(arr, n))
