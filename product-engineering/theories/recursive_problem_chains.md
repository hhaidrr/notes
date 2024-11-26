# Recursive Problem Chains 

The theory of recursive problem chains are that there are always disadvantages that come with new solutions. Every modern solution or previously modern solution
is not perfectly net valuable. There is always a qualitative disadvantage that is introduced. This means that recursively, solutions, solve problems, but as a trait
of this world (a world that requires costs), breed other problems. If this is true, this would be an invaluable insight to recursively progress along a chain of 
problem-solution pairs. This is currently just a hypothesis which needs testing and research to solidify.

Examples:
- Social media -> Dopamine control apps
- Currency -> Banks
- Banks -> DeFi
- Bitcoin -> Stablecoin

Being able to abstract which problems arise from abstract solutions give the ability to easily spot new problems.

So with both sides of the situation (problem, solution) we can make forward progress. (Problem -> solution -> problem -> solution)

## Nesting
Problems should not be naively thought of as being single layered. Like any state structure or algorithm, it is likely to have many layers and pieces. We can 
call this a composite (based off of the composite pattern). If a problem is a composite, the solution must also be a composite, where the smallest units of 
problem-solution pairs can be reduced. This way we can use the visitor pattern at the lowest unit of a problem and traverse back to the root. This would 
allow us to generate composite solutions. Looking at this inversely, we can also create composite problems from composite solutions. Again, this is a very
naive way to structure problems, but it is a first perspective.
