# quickselect

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [quickselect](#quickselect)
    - [Pseudocode](#pseudocode)
    - [Proof of correctness](#proof-of-correctness)
        - [Invariant](#invariant)
        - [Starting](#starting)
        - [Maintenance](#maintenance)
        - [Termination](#termination)

<!-- markdown-toc end -->

## Pseudocode
```
function quick_select(arr[1...n], lo, hi, key)
    pivot = array[lo]
    mid = parition(arr[1...n], lo, hi, pivot)
    
    if lo < hi then
      if mid < key:
          return quick_select(arr[1...n], lo. mid-1, key)
      else if mid > key:
          return quick_select(arr[1...n], mid+1. lo, key)

      else:
        return arr[key]
    else:
      return arr[key]
```

## Proof of correctness

### Invariant
* Invariant of partition: At all stages of quick select, the pivot is always in the correct position.
* Invariant of quick select: At all stages of quick select, the key always lies between lo and hi.


### Starting
* At the start as long as k <= hi and k is larger than lo, then there must be a kth element between lo and hi.

### Maintenance
* After partitioning with respect to pivot, index of pivot must be in correct position. 

* If kth element < index of index of pivot, the element is to the left of the index of pivot. 

* If the kth element > the index of pivot, kth element must be to the right of index of pivot. 

* If k == index of pivot, then simply return the pivot which is the right value.

* Therefore the invariant is maintained.


### Termination
Case 1: Pivot is identified to be the key
* The code terminates.

Case 2: Pivot terminates because hi > lo:
* The code terminates and return array[k]. This is because the array is sorted having finished quicksort. So as long as lo <= k <= hi, the kth value is array[k]
