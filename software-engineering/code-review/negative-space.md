# Negative Space Programming Review Guide
## Exceptions (Can be true or false, known unknowns, handleable)
Definition: Errors that are expected to happen eventually. They are external to the logic and recoverable. 
Make sure all known fault sources are adequately handled.

1. Input Validation: Are we "Sanitizing at the Gate"?
Check: Every public API or user entry point must have a schema check.

2. Transient Faults (The "3 Rs"): Retry, Relocate, or Report.
Check: For network calls, is there a jittered exponential backoff?

3. Resource Exhaustion: What if the disk is full or the thread pool is saturated?
Check: Use Bounded Queues and Timeouts. Never wait indefinitely.

The "Medicine": For every exception, is there a clear recovery path?
Check: If a write fails, is the local state rolled back or marked as "stale"?

## Invariants (Must always be true, unknown unknowns, un-handleable)
Definition: Rules that must hold true for the system to be considered "sane." If these are violated, the logic is broken.

We should include invariant checks in our code to prevent corrupt state from progressing through the program and causing silent data corruption from poisoning our IO (network, disk).
Invariant violations should cause a termination of that state scope of the program to terminate corrupt state from spreading. 
Much like cutting out a tumor before it spreads. 

The "Tumor" Principle (Fail-Fast)
Scope Termination: If an invariant fails, crash or isolate. Do not attempt to "fix" the state; it is already poisoned.

This is in-line with NASAs principles of safety critical software.

There are different types of invariants:
- Static
- implicational
- structural
- transitional
- liveness

Somewhere within these live business invariants and sanity invariants


We must strive for adequate assertion density, NASA aimed for at least 2 per function.

