
from git import Repo
from gitdb import GitDB
import os

class Repository:
    """
    """

    repo = Repo(os.getenv("PROJECT_DIR"), odbt=GitDB)
    git = repo.git
    default_branch = os.getenv("DEFAULT_BRANCH")
