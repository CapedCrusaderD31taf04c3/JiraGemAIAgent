# -*- coding: utf-8 -*-
# Copyright 2024 JiraGemAIAgent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import os

class PRCreator:
    """
    A class for creating pull requests on GitHub repositories.
    """

    def __init__(self, title: str, body: str, head_branch: str) -> None:
        """
        Initialize the PRCreator object with necessary information

        param title: The title of the pull request
        type title: str

        param body: The body content of the pull request.
        type body: str

        param head_branch: The name of the branch to merge from.
        type head_branch: str
        """

        self.title = title
        self.body = body
        self.head_branch = head_branch
  
    @classmethod
    def prepare_url(cls) -> str:
        """
        Prepare the URL for creating a pull request.

        return: The URL for creating a pull request.
        rtype: str
        """

        url = (
            "https://api.github.com/"
            f"repos/{os.getenv('REPO_OWNER')}/"
            f"{os.getenv('REPO_NAME')}/pulls"
        )

        return url

    def prepare_payload(self) -> str:
        """
        Prepare the payload for creating a pull request

        return: The payload in string format
        rtype: str
        """

        payload = {
            "title": self.title,
            "body": self.body,
            "head": self.head_branch,
            "base": os.getenv("DEFAULT_BRANCH")
        }

        return str(payload)
    
    @classmethod
    def prepare_headers(cls) -> dict:
        """
        Prepare the headers for making the API request.

        return: The headers dictionary.
        rtype: dict
        """

        headers = {
          'Accept': 'application/vnd.github+json',
          'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
          'X-GitHub-Api-Version': '2022-11-28',
          'Content-Type': 'application/x-www-form-urlencoded'
        }

        return headers

    def create_pull_request(self) -> requests.Response:
        """
        Create a pull request on the GitHub repository

        return: The response object if the request is successful, else None.
        rtype: requests.Response
        """

        response = requests.request(
            "POST", 
            url=self.prepare_url(), 
            headers=self.prepare_headers(),
            data=self.prepare_payload()
        )

        return response
