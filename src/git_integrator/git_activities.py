
from .git_repository import Repository
from .create_pr import PRCreator
import re

class GitActivity(Repository):
    """
    contains methods for the various git activities
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
        prepares branch name by combining ticket id and ticket title

        param ticket_id: id of the ticket
        type ticket_id: int

        param ticket_title: title of the ticket
        type ticket_title: str
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
        assigns branch name to the class variable

        param ticket_id: id of the ticket
        type ticket_id: int

        param ticket_title: title of the ticket
        type ticket_title: str
        """

        self.branch_name = self.prepare_branch_name(
            ticket_id=ticket_id, 
            ticket_title=ticket_title
        )

        self.git.branch(self.branch_name)
        return self

    def checkout_to_branch(self, branch_name):
        """
        checks out to the given branch

        param branch_name: name of the branch
        type branch_name: str
        """

        self.git.checkout(branch_name)
        return self
    
    def pull_changes(self):
        """
        pulls changes from git
        """

        self.git.pull()

    def stage_changes(self):
        """
        stages the changes
        """

        self.git.add(".")
        return self
    
    def commit_changes(self, commit_message):
        """
        commits the changes with the given commit message

        param commit_message: the commit message
        type commit_message: str
        """

        self.git.commit(m=commit_message)
        return self


    def push_changes(self):
        """
        pushes the changes
        """

        self.git.push("origin", self.branch_name)

        return self
    
    def create_pr(self, description=""):
        """
        creates pr with the given description

        param description: description for the pr
        type description: str
        """
        PRCreator(
            title=self.branch_name, 
            body=description,
            head_branch=self.branch_name
        )
