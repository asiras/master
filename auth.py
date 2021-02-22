import os
from pprint import pprint
import requests
token ='c1e12b1a76b94738d966f978c19726438ef6bd87'

headers = {'Authorization': 'token ' + token}

login = requests.get('https://api.github.com/user', headers=headers)
pprint(login.json())
#res=requests.get('https://api.github.com/users/asiras/repos')
#pprint(res.text)


#pygithub library
# from github import Github
# import os
# from pprint import pprint
# import urllib3
# token ='c1e12b1a76b94738d966f978c19726438ef6bd87'
# g = Github(token)
# for repo in g.get_user().get_repos():
#     print(repo.name)

# repo = g.get_repo("asiras/master")
# print(list(repo.get_branches()))

# print(repo.get_branch(branch="main"))
# print(g.get_user())

from github import Github

access_token = 'c1e12b1a76b94738d966f978c19726438ef6bd87'
g = Github(access_token)

repo_list = [i for i in g.get_user().get_repos()]
for i in repo_list:
    repo_name = str(i).replace('Repository(full_name="', '')
    repo_name = str(repo_name).replace('")', '')
    print('https://www.github.com/' + repo_name)


# import requests
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/'+username+'/repos')

# json = request.json()
# for i in range(0,len(json)):
#   print("Project Number:",i+1)
#   print("Project Name:",json[i]['name'])
#   print("Project URL:",json[i]['svn_url'],"\n")
