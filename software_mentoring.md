# Procedural
Global state 
any function can mutate any variable
became hard to scale and highly painful to debug

# OOP
solved the immediate issues of procedural programming
programs are organized around objects and methods (actions with those objects)
heavily relying on encapsulation, inheritance, polymorphism, and abstraction

OOP inherently binds data and behavior together. When multiple parts of an application touch and modify the same object, it creates a "web of dependencies." This makes tracking down bugs incredibly difficult in large, asynchronous systems.

Inheritance heirarchies are rigid and inflexible, they make adding new types easy only if they the behavior is expected 
to stay stable. Changing the heirarchy and its contracts is very painful.
OOP can union things, but it can't intersect them. If I want some properties from Class A and some from Class B, but 
not both, I have to completely restructure the heirarchy. Composition is a superset of inheritance, you start with 
1 layer of primitive building blocks and can compose them in any which way. logic is decoupled from data, and there 
are no heirarchies to adhere to.

Concurrency Nightmare: Modern software relies heavily on multi-threading and async operations. Because OOP objects easily mutate state, running them across multiple threads requires complex locking mechanisms (like mutexes), which tank performance and cause deadlocks.

# Functional programming 
Programs are constructed by applying and composing pure functions. It treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data.

Immutability by Default: Once a data structure is created, it cannot be changed. If you want to modify a list, you return a new list. This completely eliminates a massive category of bugs related to unexpected state changes.

A pure function will always return the exact same output given the same input, and it does not alter anything outside its scope (like writing to a database or changing a global variable).

What this buys you:
Fearless Concurrency: Since data is immutable, multiple threads can read the same data at the same time without any risk of data corruption. No locks needed.

Trivial Testing: Testing a pure function requires zero mocking. You pass an input, you assert the output.

Predictability: The codebase becomes deterministic. What you see is exactly what you get.

# Functional-lite
Pragmatism over purity. It adopts the best, most impactful patterns of functional programming (immutability, pure functions, composition) inside multi-paradigm languages (like JavaScript/TypeScript, Python, Kotlin, and Rust) without strictly forbidding side effects everywhere.

The "Functional Core, Imperative Shell" Architecture: This is the ultimate functional-lite pattern. You write the vast majority of your business logic using pure, predictable functional code (the core). You push all the messy, unpredictable stuff—like API calls, database writes, and UI rendering—to the very edges of your application (the shell).

Best of Both Worlds: You get 80% of the safety and concurrency benefits of pure FP, but you keep 10% of OOP's comfort (like using syntax that looks familiar to most developers).

Readability & Maintainability: Code flows logically from top to bottom through function composition or piping, rather than jumping erratically between deeply nested object instances.


Key benefits of Functional-lite:
Flexibility
- composition adapts far better to rapidly changing business requirements over inheritance heirarchies
-- heirarchies try to express the business domain, but if they get it wrong, they're very difficult to refactor
- you do not need to construct a whole class just to use a function. This makes them invokable in many more contexts
for re-use, and makes testing much easier.

Simplicity
- lack of side effects 
- clear control flow path

1. The Expression Problem (Pragmatic Adaptation)
The OOP Nightmare: In OOP, adding a new behavior across existing types is painful. If you have an Invoice class and a Receipt class, and the business suddenly demands a generateAuditLog() feature for both, you have to modify the interface or abstract class, forcing changes down the entire inheritance tree.

The FP Solution: In FP, data and behavior are decoupled. To add a new feature, you just write a new, isolated function that accepts that data. You don't have to touch or risk breaking any existing code.
