# Declarative interfaces

A declarative tool or interface focuses on describing the desired end state of a system 
or task rather than specifying the step-by-step instructions to achieve it. 
This approach allows users to express **what they want to achieve**, and the tool 
or interface determines **how to accomplish it**.

The opposite of declarative interfaces are *imperative* ones. Imperative interfaces require
you to describe how something should be performed, rather than tell it the end-state you
want it to achieve.

## The Value of Each
While **declarative interfaces** excel in simplicity and abstraction, **imperative 
interfaces** are more valuable in situations where fine-grained control, step-by-step 
execution, or handling complex edge cases is required.

Declarative is more valuable when you only care about a *product*, but don't care how
its *produced*. Whereas imperative is valuable when you care about the *producer*.
You may use the product or not, but then you take the role of the product user. The key
discriminator here is that

    As soon as you care about how a state is being produced, an imperative
    interface becomes useful to you. By default, we all prefer declarative, if the 
    option exists.

## Alignment with Paradise Theory

The previous statement aligns with [Paradise Theory](../paradise-theory.md) which states 
that our cardinal algorithm of *homeostasis* ultimately only cares about maintaining an 
ideal state of being.

If we extrapolate, we can infer that in paradise, everything is declarative. 
We simply intend a state we want and we achieve it at no cost to us. 
Imperative is only necessary in a world of costs. As product engineers, we prefer
to give as much declaration capability to our users as possible. This is aligned with them.


