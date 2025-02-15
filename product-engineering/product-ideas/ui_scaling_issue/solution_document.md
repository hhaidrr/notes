# The traditional read through web page is a time consuming process for a visitor. I just want to know what I want and get out.

I want to ask an AI prompt directly on the page what I want to know and only within the scope of the platform I have visited.
I want to be able to just ask it to do some capability or functionality or ask for some information without having to look 
for the actual manual controls, buttons and interactors scattered across the UI. This gets worse the more complex the UI is.

    Eg. amazon ui. https://www.amazon.ca/Fall-Love-Problem-Solution-Entrepreneurs/dp/1637746601/ref=tmm_pap_swatch_0?_encoding=UTF8&dib_tag=se&dib=eyJ2IjoiMSJ9.4z63jH8LCSrwrD4wjXu9-7fxmMUKXeiGhvDg0Mqb6fQHmCQuOgkPzjJsIboQhutA1ZkkAjke584-OjxZDsaxPA21-XNbp4dK75YzQLTTi8nl6qpaMTqq3t7megkKGdqHwsjjGo2JQ_zyTct9ds_SYas_XwtJNRa7haVFJKGHjUpcepsiSNl8cgwn_h40WCsf22VuY2UkqJ7YHBrU1iOumrtrNIuE-_3kb2AWJ-iQXBgj57ANw7b-YuLvba72uLTH792j1iLCXSayPaNaoF0XI-_pjctUrxpkqLqraSRs04rpZ6B5oEPZxhaJpMu3YaxrhoOtqAwlTPWzYsuP07nhkixlkUutb0jThgm9MBnNToMR1nMUPAiITqlLFgDlCJW41VSGD3z5_VR4Ut68oWzRcErxtnAMabjEe4ErlboeygJLCDf6PFLcBO7-5sGCou2s.VGO7WQ79Inwjxo8_xCBzQcGWoQQzCpM4Rh2FMwWGUZw&qid=1736690126&sr=8-1
    I couldn't find the save to reading list button for a couple minutes, and it ended up wasting my time.

# https://www.uipath.com/platform/automate/ui-and-api-automation
This complex platform has many pages and things its trying to tell me, I can't  just ask it what I want to know I have to go search for it.

I want to be able to embed a AI prompt or make it easy to get the company to embed an AI prompt directly in their web page. Or be able to vote for it on the platform so it drives them to do the integration.

This could get users to not have to rely soley on UI/UX designs and increase conversion/retention by getting the user to exactly what they need much faster


# AI over UI
AI merging with UI should aim to compliment traditional graphical UI as much as possible and target its downsides to being unscalable.
As UI scales, no matter how pretty it looks, the navigation, querying and interaction capabilities declines.

However, it will not fully replace UI as there are times when AI cannot give fully accurate results, in which UI acts 
as the failsafe option to perform a full check by the user.

AI bridges the passive nature of traditional UI and performs the work for the user to navigate the existing structure 
of the existing UI

This reminds us of the treesitter technology for capturing abstract syntax trees, allowing for overlay functionality.
UI automation tools like selenium, cypress, etc. have technology that allows for programattic interaction with UI structures.

We would introduce an GPT over this structure to allow for UXI, or user experience intelligence.

Together it would make the user experience complexity from what it currently is to a order of magnitude improvement.

The functionality we provide should be valuable enough to offer UXI as a service for business that dont want to invest
in the in house technology themselves.

POC test cases:
site: amazon 
prompt: I want to add this book to my wishlist.
-> page moves to the wishlist button and highlights it with a pulsing effect and arrow.
Declarative approach:
-> Right at the landing page after login, you can enter a command such as "checkout my cart" and it will perform that action
-> Show me my cart, it will load the cart page or show it withihn the prompt window 
UI's become more imperitively driven by the user as they scale in size, using a commany-query llm style prompt allows 
for a more declarative experience. Behaves more like a user driven index instead of a user driven searching activity which 
    can retain users and make their visits more efficient for them.

Can also query for developer documentation, right from the documentation page

prompt: Can this site do X 
-> navigate to it and highlight the corresponding relavanent area.

Assumed Sub-components:
These are the sub-systems I think will need to be in place to make this happen.
- Navigation API (using similar tech to UI automation frameworks, e.g. selenium, cypress, etc.)
- dataset to train context to the LLM (Be able to provide LLM functionality within scope of the web app to answer queries)
- being able to produce navigation instructions from a query to the navigation API

Other integrated services that would have a similar business model:
Intercom (Embedded AI customer service)
https://www.intercom.com/
Intercom's app landing page actually has a really kind of similar approach in their ctrl-k command pallete search which 
allows you to navigate, which saves clicks if I already know the paths, otherwise I am still searching through the whole 
list if I dont know where I want to go. It also doesnt support queries or commands.

We want to build a product like intercom but aimed ad UX an product navigation which would prevent needing to access 
customer support in the first place.

It would be less chat or conversation focused and get the user from their intent to their action as quick as possible 
by leading them through the UI and or doing things for them.

We also want to borrow from the work done for natural language command line applications. There are many open source 
projects on github which we can look at. This command-query interface applied in large web-apps and in person stores
as a primary means to interact with those services. This should offer more value the large and more complex the web-app
since navigating the service to execute intent takes more and more effort.

The interface should then allow the user to review irreversable actions before letting them commit to execution. e.g.
payment, checkouts



# Key KPIs targeted
Measuring user experience (UX) for a web app UI involves analyzing a mix of quantitative and qualitative Key Performance Indicators (KPIs). These KPIs evaluate usability, performance, engagement, and satisfaction. Here’s a breakdown:

---

### **1. Usability KPIs**
These measure how effectively users can interact with the web app.

#### **Task Success Rate**
- What it measures: The percentage of users who successfully complete a given task.
- Why it’s important: Indicates ease of use and whether the UI facilitates goal completion.
- Example: Completing a purchase, signing up, or submitting a form.

#### **Time on Task**
- What it measures: The average time users take to complete a task.
- Why it’s important: Shorter times often indicate an intuitive interface, while longer times may signal confusion or inefficiency.

#### **Error Rate**
- What it measures: The frequency of errors users encounter while performing tasks.
- Why it’s important: High error rates may indicate poor design or unclear instructions.

#### **Navigation Efficiency**
- What it measures: The number of clicks or actions required to achieve a goal.
- Why it’s important: Reflects how streamlined the user journey is.

---

### **2. Engagement KPIs**
These measure how users interact with your web app.

#### **Click-Through Rate (CTR)**
- What it measures: The percentage of users who click on a specific element (e.g., buttons, links, or CTAs).
- Why it’s important: Indicates which elements attract attention and drive engagement.

#### **Session Duration**
- What it measures: The average time users spend on your web app during a single session.
- Why it’s important: Longer sessions may indicate engagement, but overly long times could signal usability issues.

#### **Pages per Session**
- What it measures: The average number of pages a user visits per session.
- Why it’s important: Helps assess whether users are exploring your app or bouncing after a single interaction.

#### **Bounce Rate**
- What it measures: The percentage of users who leave after viewing only one page.
- Why it’s important: High bounce rates can indicate poor first impressions or irrelevant content.

#### **Retention Rate**
- What it measures: The percentage of returning users over a period of time.
- Why it’s important: Demonstrates long-term engagement and loyalty.

---

### **3. Performance KPIs**
These measure technical aspects of the web app that impact user experience.

#### **Page Load Time**
- What it measures: The time it takes for a page to load fully.
- Why it’s important: Faster load times lead to higher satisfaction and retention.

#### **Time to Interactive (TTI)**
- What it measures: The time it takes for the page to become fully interactive.
- Why it’s important: Users need to interact with elements without delays.

#### **First Contentful Paint (FCP)**
- What it measures: The time it takes for the first piece of content to appear on the screen.
- Why it’s important: A quick FCP enhances the perception of speed.

#### **Error Rate (Technical)**
- What it measures: The frequency of technical errors like 404s, crashes, or broken links.
- Why it’s important: Technical stability is critical for a positive user experience.

---

### **4. Satisfaction KPIs**
These measure how satisfied users are with the overall experience.

#### **Net Promoter Score (NPS)**
- What it measures: How likely users are to recommend your app to others.
- Why it’s important: A high NPS indicates satisfaction and loyalty.

#### **Customer Satisfaction Score (CSAT)**
- What it measures: A direct user rating of their experience on a scale (e.g., 1-5).
- Why it’s important: Provides a quick snapshot of user happiness.

#### **System Usability Scale (SUS)**
- What it measures: A standardized survey evaluating usability with a score out of 100.
- Why it’s important: Offers a benchmark for comparison against other apps.

#### **Churn Rate**
- What it measures: The percentage of users who stop using your web app over a period.
- Why it’s important: High churn often reflects dissatisfaction or a poor experience.

---

### **5. Accessibility KPIs**
These ensure the app is usable for all users, including those with disabilities.

#### **Accessibility Compliance**
- What it measures: Adherence to standards like WCAG (Web Content Accessibility Guidelines).
- Why it’s important: Inclusive design improves user reach and satisfaction.

#### **Keyboard Navigation Usage**
- What it measures: The percentage of users navigating via keyboard instead of a mouse.
- Why it’s important: Indicates accessibility for users with motor disabilities.

---

### **6. Behavioral Analytics**
These provide insights into user behavior on the app.

#### **Heatmaps**
- What it measures: Visual representation of user interactions, like clicks, scrolls, and mouse movements.
- Why it’s important: Highlights which areas of the UI get attention and which are ignored.

#### **Scroll Depth**
- What it measures: The percentage of page content users scroll through.
- Why it’s important: Reveals whether users


# Challenges
why havent web apps integrated ai prompts in their webpages?

1. Technical and Integration Challenges
Complexity in Integration: Incorporating AI models (like GPT-4 or other large models) into web applications involves technical challenges. It requires APIs, specialized infrastructure, and managing data flows between the web app and AI models in real time. This often necessitates significant backend changes and additional resources.
  
Latency and Performance Issues: AI prompts, especially those based on large language models, often require sending data to external servers (e.g., OpenAI’s servers) and waiting for responses. Depending on the complexity of the model and the volume of requests, this can introduce latency that negatively impacts user experience, especially for time-sensitive tasks.

2. Cost and Resource Considerations
API Usage Costs: Integrating AI models via APIs, like OpenAI’s GPT, can be expensive, especially for web apps that experience high traffic. The cost per request can add up quickly, making it challenging for many businesses to implement AI at scale without passing these costs onto users.
  
Computational Demands: Running AI models requires significant computational resources, which could add cost and complexity for the server infrastructure. Web apps may hesitate to implement this feature without a clear return on investment.

---

3. Data Privacy and Security Concerns
Sensitive User Data: Sending user inputs (which could contain personal, confidential, or sensitive information) to external AI services raises privacy concerns. Businesses must ensure that they are compliant with privacy regulations (such as GDPR, CCPA), which can be challenging when relying on third-party AI models.
  
Trust and Transparency: Users may not feel comfortable interacting with AI systems that process their data externally. There could be a lack of trust if the data used to generate AI responses isn't handled transparently or securely.

---

4. Ethical and Content Control Issues
Accuracy and Misinformation: While AI models like GPT are powerful, they are not infallible. They can sometimes produce inaccurate or misleading information, which could lead to user frustration or even harm, especially in applications like finance, health, or legal advice.
  
Moderation and Content Quality: Ensuring that AI-generated content meets quality standards or aligns with a web app’s brand voice is a challenge. It's also important to avoid generating offensive or inappropriate content, which requires robust filtering and content moderation systems.

---

5. User Experience and Interface Design
User Familiarity: Many web apps are designed to cater to traditional user interfaces, and adding AI prompts could overwhelm or confuse users who are not familiar with this technology. There may also be resistance from users who prefer a simpler, more predictable experience.
  
UI Complexity: Integrating AI prompts into a web interface in a way that feels natural and seamless without cluttering the interface is a challenge. Overloading users with too many AI features, or not properly guiding them on how to interact with AI, could negatively impact usability.

---

6. Misalignment with Business Objectives
Lack of Clear Use Case: Many web apps might not have a clear need for AI-driven prompts. For instance, basic tasks like shopping, reading content, or browsing don't necessarily benefit from conversational or automated interactions. Without a strong use case, businesses may not see the value in integrating AI.

Resource Allocation: Web apps, particularly small to medium businesses, may prioritize other features (like performance optimization, mobile responsiveness, or user support) over integrating AI due to budget, resource, or time constraints.

---

7. Regulatory and Compliance Issues
Compliance with Industry Standards: In some industries, the integration of AI-driven prompts could raise regulatory concerns, particularly when the AI interacts with sensitive or legally regulated data (e.g., healthcare, finance, and education). Businesses might need to invest in compliance measures, audits, or certifications, which could delay or prevent adoption.

---

8. AI is Still Maturing
Technology Limitations: Although AI technology, especially large language models, has made huge leaps, it still has limitations in understanding nuance, context, or intent in a human-like way. Businesses may hesitate to use AI-driven interactions if they believe the technology is not yet reliable or accurate enough for their specific use cases.

User Expectations: Users may not yet fully understand or trust AI-generated responses. AI is still in a phase where people might expect it to handle tasks perfectly, which isn't always the case. This can create a disconnect between what users expect from AI-driven interactions and what the technology can deliver.

---

9. Competition with Traditional Interfaces
Established UIs and Workflows: Traditional interfaces like buttons, forms, dropdowns, and menus are well-understood, intuitive, and often simpler to implement. In many cases, businesses might find it more efficient and effective to stick with these proven methods rather than experimenting with AI-driven interactions.

AI as an Overkill: For some web apps, the tasks being done are straightforward (e.g., online shopping or news reading), and AI-based interaction feels like an overcomplication. There's no clear benefit from AI in these cases, so businesses might not invest in such integrations.

---

Examples of Web Apps Integrating AI Prompts
Although it’s not widely adopted across all web apps, there are notable examples where AI prompts are being used effectively:
- Notion AI: Notion integrates AI prompts within its note-taking and knowledge management system to assist with writing, summarization, and brainstorming.
- Shopify's Virtual Assistant: Shopify provides AI-driven customer support and backend management tools, enabling store owners to interact with their platform through conversational prompts.
- Figma with AI Plugins: Designers can use AI-powered plugins within Figma for tasks like auto-generating content or creating layouts.

---

### **Future Trends**
Improved AI Accessibility: As AI models improve and become more affordable to integrate, we’ll likely see more web apps adopt AI-driven interactions, especially in areas where AI can provide significant value (e.g., customer support, content generation, or analytics).
  
Hybrid Interfaces: Many platforms may start integrating hybrid interfaces where users can still rely on traditional UIs but also use AI-driven prompts when they want a more personalized or automated experience.

---

### **Conclusion**
AI-driven prompts have enormous potential to transform web applications, but due to technical challenges, resource constraints, privacy concerns, and user experience complexities, their widespread adoption has been slow. However, as the technology matures and costs decrease, we are likely to see more web apps integrating these features in ways that enhance functionality without compromising performance or usability.

Would you like to dive deeper into specific AI integrations or explore examples of how certain industries might benefit from AI-driven web app interactions?
