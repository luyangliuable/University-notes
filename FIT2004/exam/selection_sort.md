# Selection sort algorithm
# Selection sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Selection sort algorithm](#selection-sort-algorithm)
- [Selection sort](#selection-sort)
    - [Pseudocode](#pseudocode)
    - [Python code](#python-code)

<!-- markdown-toc end -->


## Pseudocode
```
function selection_sort(arr[1..n]):
    for i in 1..n doj:
        min = i
        for j in range i+1..n do:
            if arr[j] < min:
                min = j
                
        if j != i:
          swap(arr[i], arr[min])
```


## Python code
```python
def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

## Time complexity
O(n^2)


## Proof of correctness

### Invariant
* Given left part of array L[1...k] and right part of array[k+1...n], the left part always contains the k smallest values in sorted order.


### Starting
* Left part of the array L[1...0] is empty so it contains no value so it is correct


### Maintenance
* Each iteration, the code seeks for the smallest value in the right unsorted part array[k+1...n] and append as k+1th value in the left array while also increasing its size by 1 and left part decrease its size by 1

### Termination
* The algorithm terminals when left part of array becomes array[1...n] where k = n and there are no value left to search hence resulting in a sorted array.
* Therefore the algorithm is correct
