import random
import time

def insertion_sort(arr: list) -> list:
    res = arr

    for i in range(1, len(arr)):
        key = res[i]

        j = i - 1
        while j >= 0 and key < res[j]:
            res[j+1] = res[j]
            j -= 1

        res[j+1] = key

    return res


start = time.process_time()
for _ in range(1000000):
    test = []
    for _ in range(25):
        test.append(random.randint(1,20))

    res = insertion_sort(test)
    # print(res)

time = time.process_time() - start
print("It took", str(time) + "s", "to run selection_sort")


