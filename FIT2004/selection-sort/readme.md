# Selection sort

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

1. array[1..i-1] is sorted
2. For any x in array[1...i-1] and y in array[i..n], x<=y
