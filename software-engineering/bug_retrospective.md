# Bug retrospective
# Bugs in stuff I built
1. Pillar violated
unhandled exception
credit card fees info was null

2. Design flaw
I decided to raise an exception, knowing there was no way to handle it and its not an invariant check

3. What should have been the design choice?
Instead of raising an error that is a sitting time bomb for me later, I should have made it impossible for those values to be null in this case.
We anticipate and allow nullibility as a branch here for those values instead of placing integrity constraints on them.



# Bugs not in stuff I built

