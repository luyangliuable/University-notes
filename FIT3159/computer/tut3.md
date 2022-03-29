# FIT3159 Tutorial 3

## Question 1 
### a

Ripple Adder need to wait for all previous bits to be added before carrying on with the next bit. 

The Ripple Adder is often cheaper than CLA adder and can increase heat dissipation.

### b
The Carry Look-Ahead adder performs all the adding of bits simultaneous so it is a lot faster. The time to complete the add operation for a ripple adder is proportional to the number of bits in the operation while the carry look ahead adder uses combinatorial logic to find the carries before the sums are calculated. The Carry Look-Ahead adder does not compute in proportional to the number of bits in the two numbers being added.

### c
Shift-add multipliers perform multiplication with only adding and shifting operations while tree multipliers performs multiplication using combinatorial logic. This is done by getting the partial products of two numbers being multiplied together and then summing to get the product. 

The tree multiplier is often more efficient but more expensive than the add and shift multiplier. The tree is now employed in most modern computers.

### d
The tree multiplier is often more efficient because it performs multiplication using combinatorial logic and it requires less operations than shifting and adding that of shift/add multiplier. 

