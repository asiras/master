from git import Repo
from getpass import getpass
username=input("enter git username :")
password=getpass()
remote = f"https://{username}:{password}@github.com/asiras/master.git"
full_local_path="D://test_git1//"
#Repo.clone_from(remote, full_local_path)