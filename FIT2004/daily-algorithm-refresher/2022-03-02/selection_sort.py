import random
import time

def selection_sort(arr: list) -> list:
    res = arr

    for i in range(len(res)):
        min = i
        for j in range(i+1, len(res)):
            if res[j] < res[min]:
                min = j

        # Invariant says that the unsorted list contains the next smallest value
        res[min], res[i] = res[i], res[min]

    return res

start = time.process_time()
for _ in range(100000):
    test = []
    for _ in range(25):
        test.append(random.randint(1,20))

    res = selection_sort(test)
    # print(res)

time = time.process_time() - start
print("It took", str(time) + "s", "to run insertion_sort")


