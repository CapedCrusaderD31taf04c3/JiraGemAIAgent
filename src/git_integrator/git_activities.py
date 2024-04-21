
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
