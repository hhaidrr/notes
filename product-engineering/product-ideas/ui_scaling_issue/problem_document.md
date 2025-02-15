# Problem Document - Large Web Apps, Poorly scaled UIs

## Central Argument
As the capabilities of an application grows, UIs become more nested. Increasing learning curves for users over time.
Thus UX decreases over time despite UI best practices. 

User intent execution gets slower over time, requires more knowledge of the product interface to compensate. The UX should take 
the load of this rather than the user to compensate for the scale of its own growing capabilities. The user should only have to 
describe their intent. Therfore maintaining a constant value for UX over time. Declarative is better than imperative.

## Observations
### Professional Users vs. Non-Professional Users
Professional users who have to use large applications for their work are expected to invest in their learning curves. 
Thus lies their paid skill. This is meant to target consumer applications which are used outside a professional context. 
However, this problem pains both types of users, thus solving would be valuable to both.

### Other Innovations Due to the Scaling Issue
Other technical needs have had to be addressed by the problem of scaling web applications in all areas such as 
the need of typescript over javascript to scale web-apps more efficiently. This addressed developer experience 
rather than user experience due to the same issue. 

### Original GUI Philosophy Remains the Status Quo
Common UI components buttons, dropdowns, modals, carousels, and navigation menus were ideated at a time when applications
were smaller scale. Frameworks to develop these UIs have matured and improved, but the design philosophy of using these 
components to facilitate user-to-application interfacing still hasnt changed from that time. 

## Example
One day I was on Amazon to look for a book which I wanted. I saw it was not available yet but was coming soon, so I wanted
to put it in my wishlist. 
I ended up spending ~5 min searching for the wishlist button despite being a long-time user of Amazon. This was the origin
of my gripe with current UI status quo. It should not take that long to convert my intent to execution. 

Using ChatGPT for this kind of use-case would give a very generic answer and may be out of date due to its dataset. 
Searching documentation and forums would add minutes and breaks the users application experience.

UIs are better or worse ultimately by the rate at which a common user can convert their intent to execution. Well-designed
UIs result in better UX which really just means users can get their task done faster because the controls are easily understandable.
The typical way to improve UI/UX is through visual architectures. Whitespace, visual heirarchy, layout strategy, etc.

This is fine for a small scale app with at most a handful of pages, each page avoiding visual clutter, however, 
the problem pain scales as more pages are added to an application as the feature-set of the app grows. Nesting and 
widening of the interaction set of the application is unavoidable if using the inherited control panel style interfaces
we are used to.

## Current Best Solutions
The current solutions to aid this pain are elements such as search bars, and more advanced fuzzy searchers like ctrl-k 
This gets you through different pages and where you need to go. This narrows search experiences, but there is still work 
involved to find the rough area you are looking for if there are many similar matches. Once on the page, you still have 
to take imperative step-by-step to execute what you want.

The only AI solution I've seen at scale is Intercom's customer service AI which you can ask product questions and 
perform some basic actions. However that does not focus on this problem, it focuses on customer service. You cannot use
it to control the application itself. It only covers general product queries and customer support workflow execution like 
creating tickets on your behalf.

Some products have created their in-house AI tools to help users with using their product like Amazon Rufus, Shopify, 
Figma etc, but this requires in-house expertise and is not easy to replicate for smaller companies. Thus it should be 
abstracted in a SaaS solution.

The command portion is what AI agents are aiming to do like Anthropic. However it is still in r&d phase and is trying to 
tackle very general commands over a whole computer system. Not specific per product or tool.

Checksum.ai can generate Cypress, Playright tests using an AI Agent

## Ideal Solution
To make current UI based interfaces feel significantly slower and frictionful to use than the implemented alternative. 

To allow the user to describe their intent (commands & queries) in natural language at a very specific or scope 
(add to cart, show me my cart items, where is the wishlist) or large scope (How would the advanced plan compare over 
a three month period compared to the basic plan). The implementation is able to execute and propose actions which 
would satisfy the user's intent with very high accuracy.

It should significantly reduce the occurence rate of users reaching for external help like chatgpt, forums, customer support 
It should significantly reduce the time it takes for them to complete their task.








