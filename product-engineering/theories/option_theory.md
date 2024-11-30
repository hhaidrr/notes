# Option Theory

We know that every algorithm have pros and cons. These pros and cons make it optimal for a set of 
use-cases while being sub-optimal for others.

We know that in recursive problem chains, the con of one product becomes the oppurtunity 
for the next. If this chain keeps going, we end up with many **options** of algorithm which each
solve a certain problem on their own. However a set of algorithms which each solve a con 
from a sibling algorithm, together they cover a wider surface area of a general problem set.

Often we say that we will use one tool for something and another tool for something else. They 
solve each others cons. However, the oppurtunity lies in unsolved cons. Meaning there is 
a lack of alternative **option** to a given con. That is where the gap in problem coverage can
be identified and *vertical* progress can be made.

This relates to the tool that finds the optimal algorithm:
(Product Idea Doc)[../product-ideas/service_locator.md]

## Recursive Problem Chains 

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

