import random
import sys

sys.path.insert(0, "/Users/rubber/University-notes/FIT2004/assignments/")
import local_max as lm
import local_maximum_wrong as lm2

n = 8
counter = 0
delay = 1

with open('fuzz_res.txt', 'w') as f:
    while True:
        if counter == 100:
            break
        arr=[[0]*n]

        for _ in range(1, n):
            arr = arr + [[0]*n]

        for i in range(8):
            for j in range(8):
                arr[i][j] = random.randint(1,999)


        lm_res1 = lm.find_local_max(arr)
        lm_res2 = lm2.find_local_max(arr)

        if lm_res1 != lm_res2:
            for _ in range(n):
                f.write(str( arr[_] ) + "\n")

            f.write("different results: first: " + str(lm_res1) + "second: " + str(lm_res2) + "\n")

        counter += 1

