import git
from git import Repo
import os.path

remoteurl="git@github.com:sakalasabareesh/gitpython.git"
localfolder="/tmp/gitpythondemo"
myrepo=git.Repo.clone_from(remoteurl,localfolder)
myrepo.git.checkout("main")

'''def test_add_file_and_commit(self, rw_dir):
        

        repo_dir = os.path.join(rw_dir, "New-directroy")
        file_name = os.path.join(repo_dir, "new-file")

        r = git.Repo.init(repo_dir)
        # This function just creates an empty file ...
        open(file_name, "wb").close()
        r.index.add([file_name])
        r.index.commit("initial commit")'''
