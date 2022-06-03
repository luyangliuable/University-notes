# insertion. sort algorithm
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [insertion. sort algorithm](#insertion-sort-algorithm)
    - [Pseudocode](#pseudocode)

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
