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
from logger.custom_logger import Logger
from typing import TypeVar

GitActivity = TypeVar("GitActivity")


import re

class GitActivity(Repository):
    """
    A class representing Git activities on a repository.
    """

    def __init__(self):
        """
        Initialize GitActivity object and perform initial operations.
        """
        self.git.checkout(".")
        self.git.checkout(self.default_branch)
        self.git.pull("origin", self.default_branch)

        self.branch_name = ""

    def prepare_branch_name(self, ticket_id: str, ticket_title: str) -> str:
        """
        Prepare a branch name based on the ticket ID and title.

        param ticket_id: The id of the ticket
        type ticket_id: str

        param ticket_title: The title of the ticket
        type ticket_title: str

        return: The branch name
        rtype: str
        """

        alphanumeric_string = re.sub(
            r'[^a-zA-Z0-9\s\\-]', 
            '', 
            f"{ticket_id} {ticket_title}"
        )

        branch_name = re.sub(r'\s+', '-', alphanumeric_string)
        return branch_name

    def create_new_branch(self, ticket_id: str, ticket_title: str) -> GitActivity:
        """
        Create a new branch based on the ticket ID and title.

        param ticket_id: The id of the ticket
        type ticket_id: str

        param ticket_title: The title of the ticket
        type ticket_title: str

        return: The updated GitActivity object.
        rtype: GitActivity
        """

        self.branch_name = self.prepare_branch_name(
            ticket_id=ticket_id, 
            ticket_title=ticket_title
        )
        if self.branch_name not in self.repo.branches:
            self.git.branch(self.branch_name)
        return self

    def checkout_to_branch(self, branch_name: str) -> GitActivity:
        """
        Checkout to a specific branch.

        param branch_name: The name of the branch to checkout
        type branch_name: str

        return: The updated GitActivity object.
        rtype: GitActivity
        """

        self.git.checkout(branch_name)
        return self
    
    def pull_changes(self) -> None:
        """
        Pull changes from the remote repository.
        """

        self.git.pull()

    def stage_changes(self) -> GitActivity:
        """
        Stage changes in the working directory.

        return: The updated GitActivity object.
        rtype: GitActivity
        """

        self.git.add(".")
        return self
    
    def commit_changes(self, commit_message: str) -> GitActivity:
        """
        Commit staged changes with a commit message.

        param commit_message: The message for the commit.
        type commit_message: str

        return: The updated GitActivity object.
        rtype: GitActivity
        """

        self.git.commit(m=commit_message)
        return self


    def push_changes(self) -> GitActivity:
        """
        Push changes to the remote repository.

        return: The updated GitActivity object.
        rtype: GitActivity
        """

        self.git.push("origin", self.branch_name)

        return self
    
    def create_pr(self, description: str = "") -> None:
        """
        Create a pull request with the current branch.

        param description: Optional description for the pull request.
        type description: str
        """
        PRCreator(
            title=self.branch_name, 
            body=description,
            head_branch=self.branch_name
        )

    def safe_eject(self):
        """
        Safely restructuring git local repositry environment
        """
        Logger.info(message="Safely Ejecting ...", stage="START")
        self.git.checkout(".")
        self.git.checkout(self.default_branch)
        if self.branch_name in self.git.branch():
            self.git.branch("d", self.branch_name)
        Logger.info(message="Safely Ejected", stage="END")