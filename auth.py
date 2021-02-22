# import os
# from pprint import pprint
# import requests
# token ='5ae7502121950f43cb65b98aa4d26f5394c87e62'

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())



from github import Github
import os
from pprint import pprint
import urllib3
token ='5ae7502121950f43cb65b98aa4d26f5394c87e62'
g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

g.get_repo('master')
