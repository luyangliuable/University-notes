import random
import time


def merge_sort(arr: list) -> list:
    res = arr
    if len(res) > 1:
        mid = len(res) // 2
        L= arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res[k] = L[i]
                i += 1
            else:
                res[k] = R[j]
                j +=1

            k += 1

        while i < len(L):
            res[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            res[k] = R[j]
            j += 1
            k += 1

    return res


start = time.process_time()
for _ in range(1000000):
    test = []
    for _ in range(25):
        test.append(random.randint(1,20))

    res = merge_sort(test)
    # print(res)

time = time.process_time() - start
print("It took", str(time) + "s", "to run selection_sort")

