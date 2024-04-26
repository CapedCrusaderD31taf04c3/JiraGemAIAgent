# GeminiDevAI

This AI system, designed to enhance software developement workflows, automates the creation of pull requests by seamlessly integrting with project management tools like Jira, It analyzes story and bug tickets, generating corresponding pull requests tailored to the specific requirements outlined in the tickets.
- Integrate GeminiDevAI properly
- Create Story or Bug Ticket in Jira
- Pull requests will be raised automatically

> Note: **GeminiDevAI** is currently supported for only Python Projects.


#### Set Environment Variables
create .env file as per fomrat in .env.template

| KEY | Description |
|-----|-------------|
| GOOGLE_API_KEY = "AI*...*xyz" | ([Get API Key](https://makersuite.google.com/app/apikey)) |
| GITHUB_TOKEN = "ghp_*.....*xyz" | ([Get Github Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)) |


Provide the repository details for the project for which you intend to create a pull request, For Examples [generative-ai-python](https://github.com/google-gemini/generative-ai-python) repository used

| KEY | Description |
|-----|-------------|
| REPO_NAME = "generative-ai-python" | Repository Name |
| PROJECT_REPO = "C:/workspace/generative-ai-python/"| Absolute path of Project Repo in local file system (path till .git folder) |
| DEFAULT_BRANCH = "main"| Default Branch of the Repository |
| REPO_OWNER = "google-gemini" | Repository Owner |

### Jira Integration

Setup webhook for activity when Issue is Created,
[Refer](https://developer.atlassian.com/cloud/jira/service-desk/automation-webhooks/)

### Prerequisite
``` shell
git clone https://github.com/CapedCrusaderD31taf04c3/JiraGemAIAgent.git
cd JiraGemAIAgent
```

### Installation
``` shell
pip install poetry==1.6.1
poetry install
```

### Start Server
``` shell
python src/main.py
```

#### License
**Apache 2.0**