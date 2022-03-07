# Merge sort
2022-03-04
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Merge sort](#merge-sort)
    - [Time and space complexity of merge sort](#time-and-space-complexity-of-merge-sort)
        - [Time complexity](#time-complexity)
        - [Space complexity](#space-complexity)
    - [Enhancement of merge sort](#enhancement-of-merge-sort)

<!-- markdown-toc end -->


## Time and space complexity of merge sort
|                 | Best case  | Average case | Worst case |
|:---------------:|:----------:|:------------:|:----------:|
| Time            | O(nlog(n)) | O(nlog(n))   | O(nlog(n)) |
| Auxiliary Space | O(n)       | O(n)         | O(n)       |

### Time complexity
The partitioning of merge sort can occur log_2(n) number of times where n is the length of the array. The depth of the recurrence is hence O(log(n)). Merging of elements however taking O(n) time, so doing this each level of recursion results in a total of O(nlog(n)) time.

### Space complexity
The auxiliary space complexity of merge sort is O(n) as the merge sort routine uses O(n) extract space for each recursion

## Enhancement of merge sort
* Merge sort can also be implemented bottom-up so the recursion will not be required all together and simply iterative merge together sub-arrays. This still requires O(n) auxiliary memory, but eliminates the use of program stack (for recursion) and hence should be slightly faster in practice.

* There are also in-place implementations of merge sort that require only O(1) space, but they are much more complicated.

## Counting inversions
