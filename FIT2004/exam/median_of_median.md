# Median of Median algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Median of Median algorithm](#median-of-median-algorithm)
    - [Pseudocode](#pseudocode)

<!-- markdown-toc end -->


## Pseudocode
```
function median_of_medians(arr[1...n], hi, lo):
    if hi - lo < 3:
        median_of_five(arr[1...n], hi, lo)
        
    // Split array into five
    
    medians = []
    for i in lo ... hi step of 5 do:
        high = min(hi, i + 4)
        medians.append(median_of_five(array[1...n], i, high))
        
    result = median_of_medians(medians[1...n], 1, n)

    return result
    
```


## Median of five:
### Pseudocode


```
function median_of_five(arr[lo...hi])
    insertion_sort(arr[lo...hi])
    // The median of an array from lo to hi is (hi+lo)//2
    return arr[( hi+lo )//2]
```

## Time complexity
* Worst case O(n) where each iteration reduces the size of array by n//5.
* Each iteration spends O(1) sorting a fixed size of 5 with median_of_five
* Therefore O(n*1)=O(1)

