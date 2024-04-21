
import requests
import os

class PRCreator:
    """
    """

    def __init__(self, title, body, head_branch):
        """
        """

        self.title = title
        self.body = body
        self.head_branch = head_branch
  
    @classmethod
    def prepare_url(cls):
        """
        """

        url = (
            "https://api.github.com/"
            f"repos/{os.getenv('REPO_OWNER')}/"
            f"{os.getenv('REPO_NAME')}/pulls"
        )

        return url

    def prepare_payload(self) -> str:
        """
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
        """

        response = requests.request(
            "POST", 
            url=self.prepare_url(), 
            headers=self.prepare_headers(),
            data=self.prepare_payload()
        )

        return response
