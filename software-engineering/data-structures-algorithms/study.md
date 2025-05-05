# problem
https://neetcode.io/problems/validate-parentheses
# what
Map
Stack
# why
We need a map to capture the associative relationships between the parentheses.
We need the stack to 
# how
Create a static map of the discrete paretheses relationships.

iterate throught the string, placing each element in the stack.
if the length of the stack is >= 2
    check if the current value i is == to the mapped value of the previous element (i-1) using the map
    if it is
        pop the last element from the stack
    else
        push the current value to the stack
if at the end of the iteration the stack is empty, then it is a valid parentheses string
else it is not a valid parentheses string


# Problem Study Framework
1. 10-15 minutes of independent attempt
2. after independent attempt, if fail, review the solution/editorial and try again
3. after independent attempt, if pass, review best solution from top rated to learn optimizations
4. Write down key takeaways
