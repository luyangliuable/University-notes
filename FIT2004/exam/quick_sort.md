# Quick sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Quick sort](#quick-sort)

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
