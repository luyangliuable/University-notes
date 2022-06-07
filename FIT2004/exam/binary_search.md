# binary_search algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [binary_search algorithm](#binary_search-algorithm)
    - [Pseudocode](#pseudocode)
    - [Python3 code](#python3-code)

<!-- markdown-toc end -->

## Pseudocode


```
function binary_search(arr[1..n], lo, hi, val): // arr must be sorted in ascending order
   
   while hi > lo: // if hi == lo this means an empty arr
    mid = ( hi+lo - 1 )//2
    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        // If val is smaller than the middle element, the target must be at the left.
        hi = mid - 1 // do not consider mid because it was already checked so there is no point
        
    if arr[mid] > val:
        // If val is larger than the middle element, the target must be at the right.
        low = mid + 1 // do no consider the mid element
        
    return null // if after the algorithm terminated and there was no result. Return nothing

```

## Python3 code

```python3
import random

def binary_search(arr: list, key: int) -> int:
    low = 0
    high = len(arr)


    while low < high:
            mid = (high+low)//2
            mid_value = arr[mid]
            print(mid, mid_value)
            if low < len(arr) - 1:
                if mid_value == key:
                    return mid
                elif mid_value < key:
                    low = mid
                elif mid_value > key:
                    high = mid
            else:
                break
    return 0


test_arr = [1,2,3,4,5,6,7,8,9,12,23,24,25,30,32]

for _ in range(115):
    print("\n")
    index = random.randint(0, len(test_arr)-1)
    print("for random index", index)
    print("result", binary_search(test_arr, test_arr[index]))

```

## Time complexity
O(log(n)) where n is the length of the array


## Proof of correctness
### Invariant
* If the middle element is the key, simply return the key and the algorithm ends 
* if the middle element is smaller than the key then search the right half of the array, otherwise right half.

### Starting
* The algorithms starts to search from the middle of the array, the only possibilities if the element exists inside it is either smaller, equal or larger than the middle element.

### Maintainence
* Each iteration the algorithm determines which half of the value must be in so it can get rid of half of the array.


### Termination
* At one iteration if the element is the middle element simply return the middle element index and the algorithm ends correctly.
* If the element to search for is not inside, the algorithms terminates when lo == hi or lo == len(arr) + 1 (empty array) from halving every time and the algorithm ends and certain that the element is not inside.
* Therefore the algorithm is correct.
