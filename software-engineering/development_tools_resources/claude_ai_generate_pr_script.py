import os
import openai
import json
from github import Github
from git import Repo
from datetime import datetime


def get_issue_details(issue_number):
    # Initialize GitHub client
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
    issue = repo.get_issue(number=issue_number)
    return issue.title, issue.body


def generate_code(title, description):
    # Initialize OpenAI client
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    Generate code based on this issue:
    Title: {title}
    Description: {description}
    
    Please provide:
    1. The code implementation
    2. A brief explanation of the implementation
    3. Any test cases if applicable
    
    Format the response as JSON with keys: 'code', 'explanation', 'tests'
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a skilled software developer who writes clean, well-documented code.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return json.loads(response.choices[0].message.content)


def create_pull_request(code_content, issue_number):
    # Initialize GitHub client
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))

    # Create a new branch
    branch_name = (
        f"feature/issue-{issue_number}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    )
    base_branch = repo.default_branch

    # Create the branch from the latest main
    sb = repo.get_branch(base_branch)
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=sb.commit.sha)

    # Create/update files
    files_to_create = {
        "implementation.py": code_content["code"],
        "tests.py": code_content["tests"],
    }

    commit_message = f"AI-generated code for issue #{issue_number}"

    for file_name, content in files_to_create.items():
        repo.create_file(
            path=f"generated/{issue_number}/{file_name}",
            message=commit_message,
            content=content,
            branch=branch_name,
        )

    # Create pull request
    pr = repo.create_pull(
        title=f"AI Generated Code for Issue #{issue_number}",
        body=f"""
        This PR contains AI-generated code for issue #{issue_number}
        
        ## Implementation Details
        {code_content['explanation']}
        
        Please review the generated code carefully before merging.
        """,
        head=branch_name,
        base=base_branch,
    )

    # Add a comment to the issue
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(
        f"Created PR #{pr.number} with AI-generated code implementation."
    )


def main():
    # Get the issue number from GitHub Events
    with open(os.getenv("GITHUB_EVENT_PATH")) as f:
        event = json.load(f)

    issue_number = event["issue"]["number"]

    # Get issue details
    title, description = get_issue_details(issue_number)

    # Generate code
    code_content = generate_code(title, description)

    # Create PR
    create_pull_request(code_content, issue_number)


if __name__ == "__main__":
    main()
