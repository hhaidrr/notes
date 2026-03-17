# Maintainability Review Guide
## Coupling & Encapsulation
Reducing how much different parts of the code rely on each other’s internal secrets.

### Law of Demeter (The "One Dot" Rule)
Definition: A method should only call methods on its own fields, its parameters, or objects it creates. It should not "reach through" an object to get to another.

Review Check: Search for "train wrecks" like order.getCustomer().getAddress().getZipCode().

Fix: The order should provide a getZipCode() method or the zip code should be passed in directly.

Functions should only operate on the things they absolutely need to do their job. All else that is passed in is unnecessary coupling.
Methods should only operate on their direct arguments and or their own object data. They should not reach into their neighbours.

### Well-Designed Interfaces
Definition: Interfaces should be "narrow" and focused on the consumer's needs, not the provider's capabilities.

Review Check: Does the interface force a client to implement methods it doesn't use? (Interface Segregation Principle).

Check: Are we leaking implementation details (e.g., a method signature that requires a specific SQL library type)?

### Dependency Inversion (DI)
Definition: High-level logic should not depend on low-level implementations (like a specific database or API client). Both should depend on abstractions.

Dependencies should be injected rather than statically created in-place.
Dependencies should come from the composition root downstream to more general parts of the system.

Review Check: Look for new keywords inside business logic classes for external services.

Check: Are dependencies injected via the constructor? This ensures the "Composition Root" controls the setup.

## Cohesion & Responsibility
Ensuring every piece of code has a clear, singular purpose.

Single Responsibility Principle (SRP)
Definition: A class or function should have one, and only one, reason to change.

Review Check: Does a single function parse data, calculate a value, and log the result to a database?

Check: Look for the word "and" in function names (e.g., validateAndSaveUser). These should be split.

Encapsulation of Logic
Review Check: Is the logic "bleeding" out? If you see the same if/else block checking an object's state in five different files, that logic belongs inside the object itself (Tell, Don't Ask).

### Extensibility (The "Open-Closed" Principle)
Making the code easy to grow without breaking what already works.

Avoiding Switch-Case Smells
Review Check: Are there massive switch statements or if/else chains checking for "Type"?

Fix: Use polymorphism or a Strategy Pattern. Adding a new "Type" should mean adding a new class, not editing a 500-line switch statement.

Configuration over Hardcoding
Review Check: Are magic numbers, strings, or URLs scattered in the logic?

Check: These should be moved to constants, environment variables, or a config object.

### State & Side Effects
Making the code predictable and easy to test.

Immutability
Review Check: Are functions mutating their input arguments? This creates "spooky action at a distance."

Check: Prefer returning new objects/collections rather than modifying existing ones.

Pure Functions
Definition: Given the same input, the function always returns the same output and has no side effects.

Review Check: Does the function rely on a hidden global variable or the current system time? If so, it’s hard to test. Pull those in as arguments.

### Cognitive Load (The "Human" Factor)
How hard is it for a tired developer to understand this at 2:00 AM?

Descriptive Naming
Review Check: Avoid generic names like data, info, or handle().

Check: Does the name describe the intent (why) rather than the implementation (how)?

DRY (Don't Repeat Yourself) vs. AHA (Avoid Hasty Abstractions)
Review Check: Is there literal copy-pasted code? (Bad).

Review Check: Is the code so "abstract" and "generic" that it’s impossible to follow the flow? (Also bad). Aim for "sensible repetition" over "wrong abstraction."

## Pure vs Side Effects segregation ((CPU, Mem) vs (Disk, Net))
Pure functions are separated from functions that handle IO (side effects).
IO functions should be as lean as possible, all smarts should be in pure functions.
IO logic should not be married to pure logic, the should be as far apart as possible.

Programming language is a resource management interface. There are the 4 colors (network, disk, memory, and cpu) and 2 textures (throughput and latency)
We need to maximize Throughput and minimize Latency by enforcing a strict separation between Business Logic (Pure) and I/O (Side Effects).

Identify the Colors: Track where the code touches Disk, Network, CPU, and Memory.
Find the Leaks: Flag any instance where Business Logic (decisions) is interleaved with I/O (side effects).
Enforce the Sandwich: If I/O happens in a loop, demand a Batch/Gulp refactor. If a logic function triggers a side effect, demand it be split into a Decider and an Actor.
Check the Texture: If I am processing a list, evaluate if I am optimizing for Throughput. If I am responding to a request, evaluate if I am minimizing Latency.
No Excuses: Do not accept 'it's easier this way' if a JOIN or a Prefetch can prevent an I/O leak."

### The Resource Checklist
Evaluate every PR against the 4 Primary Colors and 2 Textures:
CPU: Is the logic efficient? Are we doing O(n²) when O(n) is possible?
Memory: Are we allocating large objects inside loops? Is there a memory leak?
Disk/Network: Are we "Sipping" (sequential I/O) or "Gulping" (batch I/O)?
Throughput & Latency: Does this change make the system feel "heavy" or "laggy"?

IO should be done at the entry point to fetch whatever data is needed. Then that data should be passed to the pure functions.

### Review Patterns: The "Red Flags"
1. The "I/O in a Loop" (The Sip)
Detect: Any await, fetch request, or db.query inside any kind of loop.
The Fix: Instruct the user to Gather (Gulp) all data first, then pass the collection to a pure function.

2. The "Bloated Decision" (Impure Logic)
Detect: A function that performs a complex calculation but also logs to a database or sends an email.
The Fix: Separate the Decider (Pure) from the Actor (Impure).

3. The "Abstraction Leak"
ORMs (Object-Relational Mappers) are the most common source of leaks since they make side effects look like pure functions.
Detect: Using high-level sugar (like user.getOrders()) inside a performance-critical path without checking the underlying SQL/Network cost.
The Fix: Ask: "What is the physical cost of this abstraction? Does it trigger an N+1 query?"

4. Pure function returning a promise
Pure Signature: Takes raw data (Memory), returns raw data (Memory), uses only CPU.
It never returns a Promise/Future/Task. If you see a Task<T> or Promise<T> in the middle of your "Process" layer, the colors are bleeding.

5. Identify the "cost of sugar"
(Abstraction Leak), remind the reviewer 

Example: user.orders.length looks like a CPU/Memory operation, but in many frameworks, it triggers a Network call to the database.

### The "Sandwich" Architecture Enforcement
This is the Functional Core, Imperative Shell pattern
Force the code into this structure:
Gather (Shell): I/O only. Fetch all state into Memory.
Process (Core): Pure Logic only. Transform Input -> Output. No I/O allowed here.
Persist (Shell): I/O only. Save the results.


### Unavoidable Case where IO cannot be extracted out of the middle
There are only a few cases where it is necessary to require IO work to be done in between the entry and exit points of a request or runtime. 

1. Temporal dependencies (the wall)
This is the only "real" excuse. If Step B cannot be known until Step A returns from the Network, you have a Temporal Wall.
If you don't have that wall, you should be Batching/Gulping. If the pure logic only depends on our own DB, then we can prefetch what we need early.

2. Resource locking
if we have to lock a resource in order to prevent race conditions between when we made a decision and when we are performing the commit action.

3. Memory bloat
If our prefetch is too big, we can use a pipeline approach to process the data in chunks

If the user claims I/O is unavoidable (e.g., a "Pointer Chase" or "Distributed Lock"), check:

Can it be a JOIN? If yes, reject the excuse.
Can it be Parallelized? If yes, suggest Promise.all.
Is it a Stream? If the data is too big for Memory, suggest a Pipeline approach.

# The Reviewer's Mandate
- Maximize Throughput: Batch wherever possible.
- Minimize Latency: Move the data closer to the CPU.
- Segregate Side Effects: Keep the "Smarts" in the Core and the "Pipes" in the Shell.
