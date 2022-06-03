# insertion. sort algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [insertion. sort algorithm](#insertion-sort-algorithm)
    - [Pseudocode](#pseudocode)
    - [Python3](#python3)

<!-- markdown-toc end -->


## Pseudocode


```
function insertion._sort(arr[1..n]):
    for i in 2 to n do: // Start from the second element
        a = i - 1
        key = arr[i]
        while a > 1  and key < arr[a]:
            // If the current element is smaller, shift the current element right to make space.
            arr[a+1] = arr[a]
            
        a = i + 1
        arr[a] = key
```

## Python3


```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr
```
