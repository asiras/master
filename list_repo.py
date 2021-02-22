from git import Repo
username=input("enter git username :")
password=input('Enter git password :')
remote = f"https://{username}:{password}@github.com/some-account/some-repo.git"
full_local_path="D://test_git//"
Repo.clone_from(remote, full_local_path)