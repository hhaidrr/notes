# Problem Document - Language/Framework Experience Builder

## Central Argument
Many new languages and frameworks get released everyday. More are needed and wanted by either a 
product you want to build or by an employer in the job market. 

How do we try a new language or framework and really get to know it well in all its strengths and weaknesses?

Typically you would have to gain experience working with the technology in a "production" environment to really 
battle test it for what it's worth. Using something in production is also the main source of credibility to employers
that you know a technology well.

Sometimes you just want to battle test a language or framework for the fun of it to try out something new. 

To do this, I have to think of all the different use cases where the language can be used and make these applications 
from scratch. I'm not even sure which categories of characteristics I may be looking for when testing these 
technologies.

I want there to be a catalog of good application use-cases that will excercise different programmitic features of the 
language under test which I can actually then use in my day to day life and see how it performs. Technically this
requires it be viable for a production user which is yourself.

## Problem characteristics
Number of users this problem applies to (high | mid | low): mid
Frequency a user will experience this problem (high | mid | low): low

## Current Best Solutions
ChatGPT says "There isn’t a widely recognized tool or system that fully solves this problem" - 2025-02-08

# Observations
## Production Simulator
Using myself as its first and prime user for its applications are fine but it won't get close to imitating a real 
production environment. Therefore there should be an option to have a production simulator which simulates real and 
random traffic through repeatable user stories and random fuzzing. The combination of this would be closer to a production like
stress test.

## Application Project Templates 
We would need to have different application templates to choose from to apply the target language/framework.
e.g. File processor, 
multi-threaded web scraper, 
game engine,
rest api,
declarative data transformation pipeline
self hosting blog engine
dynamic code generator or plugin system
personal finance tracker with a custom query engine
peer-to-peer chat application
password manager with secure encryption

Each application would exercise different aspects or features of the language.

The features which I would want to make sure are exercised are:
### Concurrency & Parallelism
- green threads & lightweight concurrency - goroutines (go), async tasks (rust, python)
- actor model - concurrency via message passing (e.g. erlang, akka in scala)
- software transactional memory (STM) - managing concurrency via transactions (e.g. closure, haskell)
- immutable vs. mutable state in concurrency - functional languages (haskell, elixir) vs shared state (java, c++)
- lock-free & wait-free algorithms = how well does the language support non-blocking algorithms
- Asynchronous programming
- Concurrency, thread safety, event driven models

### OOP features
- class based or prototype based (java, javascript)
- encapsulation and polymorphism
- multiple inheritance & mixins

### Performance & Memory Management
- automatic garbage collection
- manual memory Management
- embedded, high performance applications

### Meta-programming & Reflection
- Macros, code introspection, runtime modifications, code generation
- Functional capabilities, immutability, monads, higher-order functions

### Networking & Real-time Applications
- Networking APIs, real-time applications, WebSockets, distributed systems
- distributed computing primitives - does the language natively support distributed computing? (eg. erlang, go)
- message passing vs. shared state (actor model, vs. traditional threading)
- RPC, & microservices support - gRPC (go, rust), akka (scala)

### Security & Cryptography
- encryption libraries, secure coding practices
- memory safety - protection against buffer overflows (rust, java, c, c++)
- sandboxing & capability-based security - can the code run in a restricted environment (e.g. WebAssembly, java security manager)


# Ideal solution
I can pick from a category of application project templates or guides and then a language I want to test, and also
the language I am most comfortable with (this chooses how the ai agent will compare how to do something in the new
language vs. how I may be used to doing it in my familiar language, and it explains why this philosphy difference is there. 



