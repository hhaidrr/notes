# End-to-End test: Fill out job application

# Arrange
Test starts already at the starting page of the job application form.
# Act 
The agent (browser-use) is able to go through the job application flow.
# Assert
static code should be able to reproduce the flow.

# Observations
The closest built in functionality to reproduce the action history statically is with
UPDATE: Yes the replay history is able to reproduce steps statically to a high degree
of success.

The initial test case presumed that the system would use the agent to generate custom API logic to interface with 
the site. However the built-in alternative is cleaner. A JSON file of the action history is saved after the agent 
performs its task. This JSON file can then be re-loaded into the application to be re-run by the static non-agentic logic
to simply replay it. This way, we are saving higher level JSON actions in files which are specific to various 
tasks rather than having full source code files per task. So as per this, the requirements of the test case are satisfied.

We proved this capability with the task of creating custom pizza. However we should test this on the actual task we 
care about which is to apply to jobs. 

Once we can replicate the capability for a flow relating to job applications, I think that is enough to pass this case.

However, from the investigation into how the agent is used, it would be better to give much more structure to our original 
prompt. It was seen that the first run of the pizza task the agent failed due to not being able to put valid address 
information in the form, instead it made up random values and hit it's failure threshhold. We then re-structured
or prompt, giving it correct address information in json format. It was able to use this and pass the address 
verification. This indicates that the more structure we give it, the better it can perform.

We should come up with a structure for job application prompting.

In general we need to provide all application information from the resume in the prompt.
"""


"""

# Other tests
The agent is able to identify whether the form is a 3rd party intermediary like workday, lever, etc.
