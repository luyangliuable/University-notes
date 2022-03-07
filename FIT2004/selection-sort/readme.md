# Selection sort

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Selection sort](#selection-sort)
    - [Key ideas](#key-ideas)
    - [Understanding](#understanding)
    - [Invariant: Selection sort](#invariant-selection-sort)
        - [Initial state of the invariant](#initial-state-of-the-invariant)
        - [Maintenance of the invariant](#maintenance-of-the-invariant)
        - [Termination](#termination)
        - [Time and space complexity of selection sort](#time-and-space-complexity-of-selection-sort)
            - [Proof](#proof)

<!-- markdown-toc end -->


## Key ideas

* Considers the list into two parts
  * The first part is currently already sorted
  * The second part consists of elements that are yet to be sorted 
  
* Initially the first sorted part is empty, while the remaining is the entire (to be sorted) list

* When sorting occurs:
  * Search for the smallest element in the unsorted part
  * swap the smallest smaller element with the first element in the unsorted part
  * the sorted part is now one element larger

```pseudcode
function selection_sort(array[1..n])   
    for i = 1 to n do
        min = i
        for j = i+1 to n do
            if array[j] < array[min] then
                min = j
            swap(array[i], array[min])
```

## Understanding

* array[1...i-1], the sorted part
* array[i..n], the yet to be sorted part


## Invariant: Selection sort

For any given value of i in the main loop of selection sort

1. array[1..i-1] is sorted
2. For any x in array[1...i-1] and y in array[i..n], x<=y

### Initial state of the invariant
* We will often use the **notation array[1..0**] (or similarly array[n+1, n]) to mean an empty array for convenience.

Initially (when i=1), the sorted part of the array array[1..0] is empty, so the **invariant trivially hold**. 


### Maintenance of the invariant

At the beginning of iteration, array[1..i-1] <= array[i..n], the value of array[min] is not smaller than any x is an element of array[1..i-1], and hence the extended sorted part array [1..i] remains sorted after swapping array[i] and array[min], so invariant 1 is maintained.

Note: if i = 1, first iteration, the sorted array is empty so array[min] is not smaller than anything in an empty array.

**The minimum element in the unsorted should always be greater or equal to the minimum element in the sorted region**. Since we are selection array[min] as a minimum array[i..n], it must be true that after swapping array[i] and array[min], so invariant 2 is maintained.

### Termination
When the i loop terminates, the invariant must still hold, and since it was maintained in iteration i=n, this implies that array[1..n] is sorted. The unsorted array is array[1..0].


### Time and space complexity of selection sort
The best, average and worst-case time complexities are all exactly the same. Selection sort always does a complete scan of the remainder of the array on each iteration. 


> The time complexity of selection sort is O(n^2)
> -- Theorem: Time complexity of selection sort

#### Proof
The number of iterations formed is n-i for each i from from 1 to n, therefore:

```Maths
n,i=1∑(n-i) = n^2 - n,i=1∑i
= n^2 - n(n+1)/2
= (n^2-n)/2
= O(n^2)
```

Only one extractor and some loop counters are needed, but **the extra space required for selection is constant**.

|                  | Best case | Average Case | Worst case |
|:----------------:|:---------:|:------------:|:----------:|
| Time             | O(n^2)    | O(n^2)       | O(n^2)     |
| Auxilliary Space | O(1)      | O(1)         | O(1)       |

