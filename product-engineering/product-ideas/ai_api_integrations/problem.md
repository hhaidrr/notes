# Problem Document - AI API Integrations

Integrating to other systems can take months long purely due to learning the other system by in house devs.

Reading docs, learning endpoints, data models, relationships, logic/behaviour. 

Having an embedded agent within the API reference which can cursorify the experience. Recipes, scripts, answering 
questions, explaining the logic and data model/relationships. This would make the dev experience much better.

Adyen API docs is where I personally felt the most pain. It was very well organized, but just the shear scale 
is unavoidable and is a good fit for LLM use-cases.


## Current Best Solutions
- Either using an AI enabled unified API such as 
    - Paragon
    - ApiDeck

- Using Cursor or dev side API tools directly.


# Observations
We can probably reverse engineer cursor but as if it were retro-fitted on an API doc

# Ideal solution
Allows general query capability which can answer questions using the general docs or the API reference as context.
Can scope different kinds of context controlled by the developer.
Can craft recipes in different languages.
Can explain the data model and relationship questions.

## Feature Backlog
