# Radix sort
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Radix sort](#radix-sort)
    - [Pseudocode](#pseudocode)
    - [Time Complexity](#time-complexity)
    - [Invariant](#invariant)
    - [Maintenance](#maintenance)
    - [Termination](#termination)

<!-- markdown-toc end -->


## Pseudocode
```
function radix_pass(arr[1...n], base, digit)
    // Same as count sort instead of counting array elements, count base
    count[0...base-1] = 0 

    // Same as count sort, figure out position of based on current digit
    pos[1...n] = 0
    
    
    for i in 1...n:
        // Since it is lsd radix sort (not hallucigen lsd), it starts from right most digit
        // get_digit gets right most digit
        count[get_digit(arr[i], digit)] += 1
        
    for v in 1...base-1 do
        // Position is in reference to current digit
        pos[v] = pos[v-1] + count[v-1]
        
    temp[1...n] = 0
    
    for each value in arr do
        // same deal as count sort but position reference digit
        digit = get_digit(value, digit)
        temp[pos[digit]] = value
        pos[digit] += 1
        
    swap(arr, temp)
    
    
function radix_sort(arr[1...n], base, digits)
    // Radix sort need to run digits amount of time
    for i in 1 to digits do
      radix_pass(arr[1...n], base, i)
```

## Time Complexity
O(k*(n+b)) where n is the elements in the array, b is the number of base and k is the number of total digits.

## Invariant
* Each iteration of radix pass, the array is sorted to the current least significant digit.
* Radix sort has same invariant as count sort but modified to sort from 1...base-1 instead of sorting in reference to array elements.


## Maintenance
* Based the more significant figure determine that overall size of the integer in reference to other integers, sorting from lsd maintains the correct position of each element in the list up to the current digit.

## Termination
* After sorting all the digits, radix continue to put emphasises on the most significant figure and finally sorting the array to the correct positions. 
