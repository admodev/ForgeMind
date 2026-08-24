# This file is used for managing git repositories to ingest data from github or gitlab.

from git import Repo

def CloneRepo(repo_url: str, local_dir: str):
    """Clone a repo to a specific path

    Parameters
    ----------
    repo_url : str
        The repo url from github.com or gitlab.com.
    local_dir : str
        The local path in the filesystem to clone the repo to.

    Returns
    -------

    git.Repo
        Repo instance
    """
    return Repo.clone_from(repo_url, local_dir)

