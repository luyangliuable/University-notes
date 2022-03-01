# Arguing Correctness
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Arguing Correctness](#arguing-correctness)
    - [Case 1: key is an element of array](#case-1-key-is-an-element-of-array)
    - [Case 2: key is not an element of array](#case-2-key-is-not-an-element-of-array)
    - [Complexity Analysis](#complexity-analysis)
        - [Theorem Time complexity of binary search](#theorem-time-complexity-of-binary-search)
            - [Proof](#proof)
        - [Common Recurrence relations](#common-recurrence-relations)
            - [Logarithmic relation](#logarithmic-relation)

<!-- markdown-toc end -->

1. Initialisation: We must prove that the **invariant hold at the beginning**
2. Maintenance: We must prove that the **invariant remain true throughout the algorithm**
3. Termination: We must prove that the **invariant remain true throughout the algorithm**


```python
import random

def binary_search(arr: list, key: int) -> int:
    low = 0
    high = len(arr)


    while low < high:
            mid = (high+low)//2
            mid_value = arr[mid]
            print(mid, mid_value)
            if mid < len(arr) - 1:
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

for _ in range(15):
    index = random.randint(0, len(test_arr)-1)
    print("for random index", index)
    print("result", binary_search(test_arr, test_arr[index]))

```

## Case 1: key is an element of array

When low and high are initialised low = 1 and high = n+1 

* If key > array[mid], low = mid, we will still have array[low] < key
* IF key < array[mid], high = mid, we will still have array[high] > key

Hence the invariant holds throughout the iteration of the loop. Therefore, if the loop terminates, it is true that array[low]  <= key <= array[hi]


## Case 2: key is not an element of array

Recall that:
```
mid = [( low+high )/2]
``` 
*Theorem* finiteness of binary search:

```
if low < high - 1, then:
    low < mid < high
```

**Proof**:

```
Since mid is the floor of (low + high)/2, it is true that:
    (low + high)/2 - 1 < mid < (low + high)/2
    
Multiplying by two, we find:
    low + high - 2 < 2.mid <= low + high
    
Since low < high-1, we have low+1 < hi. We replace low+1 with high on the right most term
    2.low < 2.mid < 2.high
and hence
    low < mid < high 

```


## Complexity Analysis 

### Theorem Time complexity of binary search
The recurrence relation (1.1) has the explicit solution
```
T(n) = a.log_2(n) + b
```

#### Proof
We will that T(n) = a.log_2(n) + b by induction on n

```math
Suppose that n=1, then a.log_2(n) + b = b which agrees with our definition of T(n)

Induction step:
Suppose that for some n, it is the case that T(n/2) = a.log_2(n/2) + b. It is then true that
    T(n) = T(n/2) + a
    T(n) = a.log_2(n/2) + b + a
    T(n) = a(log_2(n)-log_2(2)) + b + a
    T(n) = a.(log_2(n)) - a + b + a
    T(n) = a.log_2(n) + b

Hence by induction on n, it is true that:
T(n) = a.log_2(n) + b
```

### Common Recurrence relations

#### Logarithmic relation

```
T(n) = T(n/2) + a, if n > 1
T(n) = b, if  n = 1
```

#### Linear Complexity

The solution to the recurrence relation 

```
{ T(n) = T(n-1) + a, if n > 0
{ T(n) = b, if n = 0
```
Is given by:
```
T(n) = a.n + b
```

#### Superlinear complexity
The solution of the recurrence relation.

```maths
{ T(n) = 2T(n/2) + a.n, if n > 1
{ T(n) = b, if n = 1
```
is given by

```
T(n) = a.n.log(n) + b.n
```

#### Quadratic Complexity
The solution of the recurrence relation.

```maths
{ T(n) = T(n-1) + c.n, if n > 0
{ T(n) = b, if n = 0
```
is given by

```maths
T(n) = c{[n(n+1)]/2} + c.n, if n > 0```
```

#### Exponential complexity
The solution of the recurrence relation.

```maths
{ T(n) = 2.T(n-1) + a, if n > 0
{ T(n) = b, if n = 0
```
is given by

```maths
T(n) = (a+b).2^n - a
```
