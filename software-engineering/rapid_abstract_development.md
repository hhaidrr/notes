# Rapid Abstract Development 

Let's just do what all people do in software. Make acronyms. Let's call this one RAD.

## Goal
The goal of RAD is to not think of development as a whole plop of years long work to build a huge platform with a 
bunch of integrations, and network protocols, querying, infrastructure, etc. 

The idea is to start with the writing out the app's core package. This package has no details.
Only the logic which you have ideated in your mind at the core of this application.

This is very manageable. Implementation takes a long time, it takes teams and employees. 
Ideation, and expression takes much less time. 

This spreads out the iterative release process over a period of time to let it materialize it's implementations.

However, from the start we have already created the essence of our app.

Writing an idea is an order of magnitude cheaper and quicker than writing an implementation. 
The core package is the idea.

## Stick to the interfaces
In this package we define the starting interfaces that all the implementations have to comply with.
There is a concern that when it comes time to be met with reality, the implementations will force 
these interfaces to change. However, that should never happen. Otherwise the abstractions and the lose their power to reality.

The idea conforms to constraints. This must be avoided at all cost in order to preserve the original
idea of the core package.

If we scale the idea that implementations can force interfaces to change. 
Every n implementations has a chance of changing an interface. 
This means the interface is coupled to the constraints of each implementation.

The core package loses it's extensibility this way. 

If there is no direct way for an implementation to conform with a given interface. It just means
there are un-identified middle layers of abstraction required to bridge the gap.

UPDATE 2025-01-06:
After attempting RAD which is a good concept in theory, we encountered some obstacles.
I realized that there was a lack of reference for program correctness. Meaning there were no requirements. Or the 
requirements were so vague that it was hard to define what functional means at the level of code implementation.
So we decided to define unit tests as the nearest proximal form of functional definition for the program. This is ongoing.

# Starting with the view
After attempting RAD once. I realize that starting with the core package is ideal for prototyping the back-end API.
However coding a back-end API may not be the best first step in the end-to-end prototyping phase. The purpose of prototyping is to 
have a proof-of-concept to demo/test the minimal functionality of an idea. Function will require actual code.

However ideation does not require actual code. It just requires a form of expression to convey its vision. 
This is where no-code/low-code views serve their purpose. Sharing a vision is the first step of an idea in order to 
get others involved and convinced of its potential. We want to keep the ideation-to-demo-ability period as fast as possible.

Coding a core package for a back-end API and then creating a code complete view alongside it is still a months long effort 
on average. Dealing with code stacks and languages have already delved too deep into implementation detail and require a time
investment which won't even reap anything demo-able to investors or collaborators on its own. When this functional mock is 
ready in a couple months, it may flat out get rejected, or more likely most often it will get feedback the requires 
code revision. This phase is very unstable and the idea can be pivoted or changed drastically, the cost of change will
still be very high.

This is why starting out with a no-code/low-code view is much cheaper to prop-up and change afterward while being
demo-able from the start. Humans can transfer the vision and feel of an idea through visuals much better, 
and the cheapest way to do the quickest way we can make a view or "paint a picture".





