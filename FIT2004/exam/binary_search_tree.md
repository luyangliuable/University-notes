# Binary Search Tree
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Binary Search Tree](#binary-search-tree)
    - [Insert](#insert)
        - [Pseudocode](#pseudocode)

<!-- markdown-toc end -->


## Insert

### Pseudocode

```
function insert(item, node)
    if item < node.value then
      if node.left == null then
        node.left = Node(item)
      else
        insert(item, node.left)
        
    else if item > node.value then
        if node.right == null then
            node.right == Node(item)
        else
            insert(item.node.right)
            
    else:
        // Additional chaining data structure.
```

## Delete pseudocode

```
function delete(item, node)
    if node is null then
        return null

    if node.val < item then
      delete(item, node.left)
          
    else if node.val > item then
      delete(item, node.right)
    else:
      res = node.value
      swap(find_successor(node), null)
      return res
        
    return null
       
 
function find_sucessor(node)
    if node.right == null:
        return null

    n = node.right

    while n is not null do
        if n.left == null
          return n
        n = n.left
```

## Find pseudocode
```
function find(item, node)
    if node is null
        return null

    if node.value < item then
        return find(item, node.left)
        
    else if node.value > item then
        return find(item, node.right) 
        
    else
        return node.value
```
