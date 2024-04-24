
import requests
import os

class PRCreator:
    """
    contains methods to create PR
    """

    def __init__(self, title, body, head_branch):
        """
        initialises the title, body and branch for the PR

        param title: title of the PR
        type title: str

        param body: body for the PR
        type body: str

        param head_branch: name of the head branch
        type head_branch: str
        """

        self.title = title
        self.body = body
        self.head_branch = head_branch
  
    @classmethod
    def prepare_url(cls):
        """
        prepares URL for the PR using environment variables for repo owner and repo name
        """

        url = (
            "https://api.github.com/"
            f"repos/{os.getenv('REPO_OWNER')}/"
            f"{os.getenv('REPO_NAME')}/pulls"
        )

        return url

    def prepare_payload(self) -> str:
        """
        prepares payload for the PR
        """

        payload = {
            "title": self.title,
            "body": self.body,
            "head": self.head_branch,
            "base": os.getenv("DEFAULT_BRANCH")
        }

        return str(payload)
    
    @classmethod
    def prepare_headers(cls):
        """
        prepares headers for the PR
        """

        headers = {
          'Accept': 'application/vnd.github+json',
          'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
          'X-GitHub-Api-Version': '2022-11-28',
          'Content-Type': 'application/x-www-form-urlencoded'
        }

        return headers

    def create_pull_request(self):
        """
        creates pull request by using the url, headers and payload created initially
        """

        response = requests.request(
            "POST", 
            url=self.prepare_url(), 
            headers=self.prepare_headers(),
            data=self.prepare_payload()
        )

        return response
