# What do I do? 
This is a cache of pre-computed answers to common mental blocking decision points in writing code.

1. We have many database writes that are roughly the same for distinct entry point operations. Duplicating these writes
at the call sites is a violation of DRY.

We have unique way of doing something, but they all need to record their something in a standard way.
There are multiple different use-cases or workflows that end up charging a card, all of them 
need to update the database in n different unique ways in order for the operation to make the database consistent
for the next operation to pick up from.

a. Should I duplicate code across all the call sites? 
- violates DRY
b. should I put the code in a function and explicitly call the function from all the call sites?
- satisfies DRY, but requires new developers who are creating new ways of charging a card to somehow know about
the existence of this function and to call it.
c. should I fire an event that causes the reconcilation to happen? 
- same function happening somewhere else, developers still need to know to all the event trigger, more indirection

## answer: Implement a data-oriented FSM pattern, slice horizontally into (domain event, FSM, effects)
Every trigger point only knows of its domain events, it doesnt know about state machine internals or side effects.
it goes from IO to pure domain logic to pure domain DTO event, passes the domain event DTO to the FSM.
The FSM is pure as well and wires/maps business events to EFFECTs which are IO functions.
The effect is executed last.
This complies with imperative shell, pure core and organizes the horizontal seams of the application better than before. 
note: how to handle atomic IO vs non-atomic IO?



