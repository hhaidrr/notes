# Scheduled Automated Job Application Pipeline
This document outlines the requirements for an automated job application pipeline that aims to use modern 
engineering techniques and technologies to abstract the job application process completely from the user.

## Terminology
non-indexed vs. indexed site
A site that has an interaction API layer that the service has made for reliably populating fields. New companies without an index 
may result in errors with newly generated indexes.

## Success Criteria
- The automation is able to get from start to end of an application form with 0% applicant intervention 100% of the time for %100 percent of company sites.
- The automation is able to get from start to end of an application form with 90% >= success rate without a human service operator
on non-indexed company sites.
- The automation is able to get from start to end of an application form with 99% >= success rate without a human service operator
on indexed company sites.

## User View (UV)
- See a list of jobs the service is recurrently applying to
## User Capabilities (UC)
- Pull jobs from linkedIn into the recurring application list

## v1 Functional Requirements 
I can pull jobs from linkedIn with a browser plugin. Which gets populated in a list within the app.
Complete job applications with 100% accuracy and success rate at various job sites.
Re-apply at a given schedule as long as that posting exists.

## Observations/Backlog
- Handle questions that are arbitrary and unique to the job posting
e.g. describe the hardest problem you've worked on 
e.g. What is your greatest technical achievement/project
We will need to handle this in a special way since we cannot just autofill on first attempt. 
We will need to put the application in a pending state, allow the agent to come up with a generated template response, and post it to the user.
The user can then optionally edit the template using the agent to finalize the response and save it as the answer to the question.
The agent will then use this answer in the future.
