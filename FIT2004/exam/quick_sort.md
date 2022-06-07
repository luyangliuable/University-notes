# Quick sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Quick sort](#quick-sort)
    - [Pseudocode:](#pseudocode)
    - [Time complexity](#time-complexity)
    - [Proof of correctness](#proof-of-correctness)
        - [Invariant](#invariant)
        - [Starting](#starting)
        - [Maintenance](#maintenance)
        - [Termination](#termination)

<!-- markdown-toc end -->

## Pseudocode:

```
function quick_sort(arr[1..n], lo, hi)

partition = partition(arr[1..n], lo, hi)

if partition - lo != 0: // check if new partition is not len 0
    quick_sort(arr[1..n], lo, partition)

if hi - ( partition + 1 ) != 0: // check if new parition is not len 0
    quick_sort(arr[1..n], partition + 1, hi)

```

```
// Naive partition
function partition(arr[1..n], lo, hi, pivot)

    pivot_val = arr[pivot]
    swap(arr[1], arr[pivot])

    boundary = 2
    for i in lo .. hi do
        if arr[i] < pivot_val:
            swap(arr[bounday], arr[i])
            boundary += 1

        search += 1

    swap(arr[boundary], arr[1])

```

```
function dnf_partition(arr[1..n], lo, hi, pivot): // pivot should be determined in quicksort!
    mid = lo

    while mid <= hi do
        if arr[mid] > pivot then
            swap(arr[hi], arr[mid])
            hi -= 1
        else if arr[mid] < pivot then
            swap(arr[lo], arr[mid])
            lo +=1
            mid += 1
        else // mid.e. white
            mid += 1

    return lo, mid
```

## Time complexity
O(nlog(n)) worst case if pivot is in the 30% to 70% percentile or middle all the time
O(n^2) worst case if pivot is the first or last element of the sorted array all the time


## Proof of correctness

### Invariant
* Each partition, the pivot is sorted to it's correct position


### Starting
* There is no partition yet, so no pivots in correct position.

### Maintenance
* In an ideal situation, the pivot is always close to the center of the array leading to a even split for 2 additional quicksort while the pivot is in the correct position.

### Termination
* The new partition will continue to place middle element in the correct position until the length of the partition array is 1.
* At this point all the value in the array are in the correct position hence sorted
* The algorithm is correct.



