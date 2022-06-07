# AVL Tree

## rotate right

### Pseudocode

```
functional rotate_right(node)
    par = root.parent

    pivot = node.left
    tmp = pivot.right
    pivot.right = root
    root.left = tmp
    par.swap(pivot, root)
```

## Rotate left
```
functional rotate_left(node)
    par = root.parent
    
    pivot = root.right
    tmp = pivot.left
    pivot.left = root
    root.right = tmp
    par.swap(tmp, pivot)
```

## Left-Right case: Right-Left rotation

```
function left_right_rotation(node)
    rotate_right(node.right)
    rotate_left(node)
```

## Right-Left case: left-right rotation

```
function right_left_rotation(node)
    rotate_left(node.left)
    rotate_right(node)
```


## Delete
```
function delete(item, root)
    if root == null then
        return null
    
    if item < root.value then
        root.left = delete(item, root.left)
        
    else if item > root.value then
        root.right = delete(item, root.right)
    else
      if root.left is null:
          temp = root.right
          root = None
          return temp

      elif root.right is null:
          temp = root.left
          root = None
          return temp

      // Currently at the node with the value to remove
      succ = getMinValueNode(root.right)
      root.val = succ.val
      root.right = delete(root.right, succ.val) // delete the successor
            
    // Step 2. Update the height of the ancestor node
    root.height = 1 + max(self.left.height, self.right.height)
    
    // Step 3. Update the balance
    root.balance_factor = self.left.height - self.right.height
    
    
    // Step3. rebalance
    rebalance(root)
```

## Rebalance

### Pseudocode
```
function rebalance(node)
    if node.balance_factor > 1 and node.left.balance_factor >= 0:
        // left-left case, simply rotate right
        rotate_right(node)
    
    else if node.balance_factor > 1 and node.left.balance_factor < 0:
        // left-right case
        rotate_left(node.left)
        rotate_right(node)       

    else if node.balance_factor < -1 and node.right.balance_factor > 0:
        // right-left case
        rotate_right(node.right)
        rotate_left(node)
        
    else if node.balance_factor < -1 and node.right.balance_factor <= 0:
        // right-right case
        rotate_left(node)

    
```

## Insert
###
