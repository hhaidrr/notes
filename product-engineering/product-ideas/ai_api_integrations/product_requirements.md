# AI Augmented Integration Developer Experience | AI API Docs
This document outlines the requirements for an AI enabled API Integration service which augments existing API
docs and references with an AI enabled developer experience.

## Success Criteria (case-study: Adyen API)
- I can ask general questions to understand the underlying data model and its relationships
    - How is a balance account related to a transfer instrument?
    - How can I split 1% surcharge to the merchant and 4% to our company account during credit card transactions?
    - How do I use the Adyen API as a platform if I need to route funds from merchant's customers to the merchant and 
    bill a margin? Explain the models, relationships, and endpoints involved.
- I can ask it to make a API client/sdk in any language (doest apply to Adyen because they already have an SDK)
- Ask it to make recipes for me.
    - Write logic to onboard a sub-merchant with all the information they need to satisfy all the Adyen KYC requirements
    - Add payment methods after onboarding
    - Write logic on how I would top up a balance account if it goes negative due to a chargeback on an ACH transaction.
- I can scope contexts from the API reference by highlighting certain text and putting it into the context window
    - Asking questions on a specific endpoint.
    - Asking clarification from a paragraph from the general docs
    - Writing some code which can call that endpoint.
- It takes months less time to integrate with a large API than without an AI solution architect/engineer. Time-to-integrate 
benchmarks before & after using AI 
- Error rate reduction in AI-Generated code (fewer failed API calls)
- Developer engagement metrics (queries per session)
- Can switch between basic and complex reasoning models
- Cost thresholds which warn about expensive queries


## User View (UV)
- See the original API Reference. has a prompt window on top center to ask questions.
- If it is being used to write some logic or a recipe, it opens a side panel or separate page to co-collaborate with you.
- The co-collaboration window is similar to chatGPTs, it is integrated to the API doc web app for first time use and 
quick prototyping
- CLI/VS Code extension for advanced workflows.

## User Capabilities (UC)
- Can query natural language questions to a agent trained on the specific platform or API
- Can ask to write client side code snippets in any language calling the API for various workflows.

## Functional Requirements 
1. Querying and Understanding the Data Model
- Users can ask general questions to understand the underlying data model and its relationships.
- The AI will get it's context by pre-indexing all the information present on the API reference and the general docs, and
schema metadata. How it understands the context can vary as we research more.

2. Generating API Clients and SDKs
- Users can request an API client or SDK in any programming language.
- The co-collaboration/solution engineer window will allow to save, edit, export responses and have a history of previous 
work/queries.
- Developers will be able to easily retrieve their work via CLI/VS code extension
- If an official SDK already exists, the system will provide guidance on its usage instead of generating a new one.

3. Creating Code Recipes for Common Use Cases
- Users can request ready-made implementations for common workflows.

4. Context-Aware Documentation Assistance
- Users can scope relevant contexts from an API reference or documentation by selecting specific text.
- The agent can provide inline explanations, generate example calls, and link to related docs.

5. Safe-guards and enforcing best practices
- If it notices the usage of deprecated endpoints or breaking changes, it will warn the developer and suggest alternatives.
- Will warn developers about best security practices, e.g PCI scope for credit cards, PII, etc.
- The agent will monitor API version changes and notify developers about necessary updates. This aims to ensure long-term 
usability for rapidly evolving APIs.


## Non-Functional Requirements
- Response accuracy
    - All snippets produced must be runnable and correct.
    - Should encourage high number of queries per session
    - Agent cost should be effectively managed
        - Caching responses
        - Agent model and query complexity will scale dynamically based on query depth
    - It will lint and test the code before displaying it using static methods.
    - Agent generated code will include error handling as well as API calls.
    - Have a testing mechanism and feedback loop for improving snippet quality.


