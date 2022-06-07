# Balanced search tree

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Balanced search tree](#balanced-search-tree)

<!-- markdown-toc end -->

## Pseudocode


```
function init(arr[1...n])
   arr.mergesort() 
   
   bst = insert(arr, bst.root)
   return bst
   
function insert(arr[1...n])
   mid = n//2

   left = arr[1..mid-1]
   right = arr[mid+1...n]
   
   node = node(arr[ mid ])

   node.left = (left, node.left)
   node.right (right, node.right)
   
   return node
```

## Time complexity
O(nlog(n) + log(n)) = O(nlog(n)) where n is the number of element to be inserted into bst. O(nlogn) is merge sort time complexity
It takes log(n) splits for the binary tree and each split does an addition O(1) operation to store the mid value.

**This is why it could take O(log(n)) complexity while still have auxiliary space of O(n). So O(nlog(n)) time complexity could result in an auxilliary space complexity of O(n^2)**



## Proof of correctness

## Invariant
* Each recursion, smaller half of the array is to be placed to the left of the current BST node and the other larger half is to the right of the current BST node.

## Starting
* Both half of the array contain the whole bst tree element to be inserted and bst is empty so invariant is correct.

## Maintenance
* Each recursion, the bst tree is balanced by taking the middle element and by satisfying the definition of bst continuing to place the elements to the left and larger to the right.

## Termination
* The algorithm terminates with an evenly balanced bst because each recursion it takes exactly half of the larger to form a perfect binary tree.
* The algorithm is correct.
