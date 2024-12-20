# Rapid Abstract Development 

Let's just do what all people do in software. Make acronyms. Let's call this one RAD. It's pretty rad to call this RAD.

## Goal
The goal of RAD is to not think of development as a whole plop of years long work to build a huge platform with a bunch of integrations, and network protocols, querying, infrastructure, etc. 

The idea is to start with the writing out the app's core package. This package has no details.
Only the logic which you have ideated in your mind at the core of this application.

This is very manageable. Implementation takes a long time, it takes teams and employees. Ideation, and expression takes much less time. 

This spreads out the iterative release process over a period of time to let it materialize it's implementations.

However, from the start we have already created the essence of our app.

Writing an idea is an order of magnitude cheaper and quicker than writing an implementation. The core package is the idea.

## Stick to the interfaces
In this package we define the starting interfaces that all the implementations have to comply with.
There is a concern that when it comes time to be met with reality, the implementations will force 
these interfaces to change. However, that should never happen. Otherwise the abstractions and the lose their power to reality.

The idea conforms to constraints. This must be avoided at all cost in order to preserve the original
idea of the core package.

If we scale the idea that implementations can force interfaces to change. Every n implementations has a chance of changing an interface. This means the interface is coupled to the constraints of each implementation.

The core package loses it's extensibility this way. 

If there is no direct way for an implementation to conform with a given interface. It just means
there are un-identified middle layers of abstraction required to bridge the gap.



