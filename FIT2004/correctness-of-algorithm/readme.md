# Correctness of algorithm
2022-03-08
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Correctness of algorithm](#correctness-of-algorithm)
    - [Proving correctness of algorithm](#proving-correctness-of-algorithm)
        - [Invariant](#invariant)
            - [Before initialisation](#before-initialisation)
    - [Correctness using loop invariant](#correctness-using-loop-invariant)
    - [Revised binary search](#revised-binary-search)

<!-- markdown-toc end -->

## Proving correctness of algorithm
* Testing cannot **guarantee** that the program is always correct!
  * There are infinitely many possible inputs (for most programs) so we cannot test them all.

* Logic can prove that a program is always correct. This is usually achieved in two parts.
  * Show that the program **always terminates***
  * Show that a **program produces correct results when it terminates**.

Example:

Indexing starts from one! Not zero
```python

def test()
  min = array[1] 
  index = 2

  while index <= N:
      if array[index] < min:
        min = array[index]
      index = index + 1

  return min
```

  * [x] Always terminates
  * [x] Correct result when terminates 

### Invariant
#### Before initialisation
* [x] First half equals array[1 ... index - 1] so only [2] and 2 is the minimum in the array.
* [x] Each loop array equals array[1 ... index], it checks array[index] is smaller that the current minimum, if the is it currents the minimum for array[1 ... index], invariant is preserved.
* [x] TODO When loops terminates while array is array[1 ... N], the minimum is now the minimum of the entire array as array[1 ... N] is the array

## Correctness using loop invariant
* Invariant needs to be true at three points.
  * Before the loop starts (initialisation)
  * During each loop (maintenance)
  * After the loop terminates (termination)

## Revised binary search

Revised binary search

```python
lo = 1
hi = N + 1

while (low < high -1):
  mid = (low + high) // 2
  if t >= L[mid]:
      low = mid
  if < L[mid]
      hi = mid
        
if L[lo] == t
  return lo

return False
```

TODO what happens if low = hi - 1 and t >= L[mid]?

