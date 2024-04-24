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

from .git_repository import Repository
from .create_pr import PRCreator
import re

class GitActivity(Repository):
    """
    """

    def __init__(self):
        """
        """
        self.git.checkout(".")
        self.git.checkout(self.default_branch)
        self.git.pull("origin", self.default_branch)

        self.branch_name = ""

    def prepare_branch_name(self, ticket_id, ticket_title):
        """
        """

        alphanumeric_string = re.sub(
            r'[^a-zA-Z0-9\s\\-]', 
            '', 
            f"{ticket_id} {ticket_title}"
        )

        branch_name = re.sub(r'\s+', '-', alphanumeric_string)
        return branch_name

    def create_new_branch(self, ticket_id, ticket_title):
        """
        """

        self.branch_name = self.prepare_branch_name(
            ticket_id=ticket_id, 
            ticket_title=ticket_title
        )

        self.git.branch(self.branch_name)
        return self

    def checkout_to_branch(self, branch_name):
        """
        """

        self.git.checkout(branch_name)
        return self
    
    def pull_changes(self):
        """
        """

        self.git.pull()

    def stage_changes(self):
        """
        """

        self.git.add(".")
        return self
    
    def commit_changes(self, commit_message):
        """
        """

        self.git.commit(m=commit_message)
        return self


    def push_changes(self):
        """
        """

        self.git.push("origin", self.branch_name)

        return self
    
    def create_pr(self, description=""):
        """
        """
        PRCreator(
            title=self.branch_name, 
            body=description,
            head_branch=self.branch_name
        )
