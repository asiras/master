# import os
# from pprint import pprint
# import requests
# from getpass import getpass
# token =getpass()

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())
#res=requests.get('https://api.github.com/users/asiras/repos')
#pprint(res.text)


#pygithub library
# from github import Github
# import os
# from pprint import pprint
# import urllib3
# token =''
# g = Github(token)
# for repo in g.get_user().get_repos():
#     print(repo.name)

# repo = g.get_repo("asiras/master")
# print(list(repo.get_branches()))

# print(repo.get_branch(branch="main"))
# print(g.get_user())



# import requests
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/'+username+'/repos')

# json = request.json()
# for i in range(0,len(json)):
#   print("Project Number:",i+1)
#   print("Project Name:",json[i]['name'])
#   print("Project URL:",json[i]['svn_url'],"\n")


from github import Github
from getpass import getpass
access_token =getpass()
g = Github(access_token)

repo_list = [i for i in g.get_user().get_repos()]
for i in repo_list:
    repo_name = str(i).replace('Repository(full_name="', '')
    repo_name = str(repo_name).replace('")', '')
    print('https://github.com/' + repo_name)
