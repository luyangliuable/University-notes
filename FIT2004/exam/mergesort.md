# Merge sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Merge sort](#merge-sort)
    - [In-place merge sort](#in-place-merge-sort)
        - [Pseudocode](#pseudocode)

<!-- markdown-toc end -->

## In-place merge sort

### Pseudocode

```
function merge_sort(arr[1..n], lo, hi):
    mid = n//2
    
    if n = 0: // meaning empty array
        return arr
    
    left = merge_sort(arr[1..n], lo, mid)
    right = merge_sort(arr[1...n], mid+1, hi)
   
    i = lo
    j = mid + 1
    c = lo

    while i <= mid or j <= hi:
      if arr[i] >= arr[j]:
        arr[c] = arr[j]
        j += 1
      else:
        arr[c] = left[i]
        i += 1
      c += 1
        
    for leftover in i to mid do
        arr[c] = arr[leftover]
        c += 1

    for leftover in j to hi do
        arr[c] = arr[leftover]
        c += 1
        
    return arr
```
### python code
```python
def mergesort(arr):
    res = arr
    if len(res) > 1:
        # Finding the mid of the resay
        mid = len(res)//2

        # Dividing the resay elements
        L = res[:mid]

        # into 2 halves
        R = res[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp resays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res[k] = L[i]
                i += 1
            else:
                res[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            res[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            res[k] = R[j]
            j += 1
            k += 1
```
