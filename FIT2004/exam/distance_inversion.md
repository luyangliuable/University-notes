# count inversion

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Distance inversion](#distance-inversion)

<!-- markdown-toc end -->

## Naive distance inversion
### Pseudocode

```
function count_inversion(arr[1...n])

    inv_count = 0
    for i in range 1...n do
        for j in range i+1...n do
            if (arr[i] > arr[j])
                // If an element is larger than an element coming after it
                inv_count += 1
                
    return inv_count

```

## Divide and conquer distance inversion

```
function split_and_count(arr[lo...hi])
    if hi - lo == 1:
        return arr, 0
        
    mid = (hi-lo)//2
    arr_l, inv_l = split_and_count(arr[lo...mid])
    arr_r, inv_r = split_and_count(arr[mid+1...hi])
    
    inv_s = merge(arr_l, arr_r)
    
    return arr[lo...hi], inv_l+inv_r+inv_s
    

function merge(arr_l[lo...mid], arr_r[mid+1...hi])

  l = lo
  r = mid+1
  count = 0
  result = []

  while l <= mid and r <= hi do
    if r > hi or (l <= mid and arr_r[r] >= arr_l[l] ) then
        result.append(arr_l[l])
        l += 1
    else
        result.append(arr_r[r])
        r += 1
        count = count + mid - l + 1
        
        
    return result, count
```
