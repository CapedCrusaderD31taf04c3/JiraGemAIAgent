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
