# Count Sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Count Sort](#count-sort)
    - [Pseudocode](#pseudocode)
    - [Time Complexity](#time-complexity)
    - [Invariant](#invariant)
    - [Starting](#starting)
    - [Maintenance](#maintenance)
    - [Termination](#termination)

<!-- markdown-toc end -->

## Pseudocode


```
function count_sort(arr[1...n])
    count[1..n] = 0
    position[1..n] = 0
    
    for each val in arr:
        count[val] += 1
        
    position[1] = 0
    for i in 2...n:
        position[i] = position[i-1] + count[i]
        
        
    temp_arr[1...n] = 0
    for each val in arr:
        temp_arr[position[val]] = val
        position[val] += 1
        
    return temp_arr
```

## Time Complexity
O(n + u) where n is the number of elements in the array to sort and u is the size of count and position array.


## Invariant
* Count array organises the position of the item to be placed next in the array.


## Starting
* Count and position array are both created by simply counting the occurrence of element in array

## Maintenance
* Insert the array elements by looking up the next available pigeonhole for the position of element. After using the pigeonhole add one to the position array indicating the next available pigeonhole.

* Hence this allows all elements to be inserted in the correct position while maintaining the position array.

## Termination
* After all the elements are inserted correctly, the algorithm terminates.

