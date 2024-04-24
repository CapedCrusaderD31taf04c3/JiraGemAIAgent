
from git import Repo
from gitdb import GitDB
import os

class Repository:
    """
    initialises the repo and default branch for git
    """

    repo = Repo(os.getenv("PROJECT_DIR"), odbt=GitDB)
    git = repo.git
    default_branch = os.getenv("DEFAULT_BRANCH")
