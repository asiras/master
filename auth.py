# import os
# from pprint import pprint
# import requests
# token ='551a02358db8a37a25572b6716d5a498733acc9a'

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())
# #res=requests.get('https://api.github.com/users/asiras/repos')
# #pprint(res.text)


#pygithub library
from github import Github
import os
from pprint import pprint
import urllib3
token ='551a02358db8a37a25572b6716d5a498733acc9a'
g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("asiras/master")
print(list(repo.get_branches()))

print(repo.get_branch(branch="main"))
print(g.get_user())

# import requests
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/'+username+'/repos')
# json = request.json()
# for i in range(0,len(json)):
#   print("Project Number:",i+1)
#   print("Project Name:",json[i]['name'])
#   print("Project URL:",json[i]['svn_url'],"\n")

# file_path = "D://test_git//test.txt"
# g = Github(token)
# repo = g.get_repo("asiras/master")

# file = repo.get_contents(file_path, ref="main")  # Get file from branch
# data = file.decoded_content.decode("utf-8")  # Get raw string data
# data += "\npytest==5.3.2"  # Modify/Create file

# def push(path, message, content, branch, update=False):
#     # author = InputGitAuthor(
#     #     "asiras",
#     #     "asiras@gmail.com"
#     # )
#     author='asiras'
#     source = repo.get_branch("main")
#     repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
#     if update:  # If file already exists, update it
#         contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
#         repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
#     else:  # If file doesn't exist, create it
#         repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch

# push(file_path, "Add pytest to dependencies.", data, "main", update=True)