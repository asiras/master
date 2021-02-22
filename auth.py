# import os
# from pprint import pprint
# import requests
# token ='d6a2d1c8ae3de0f86fbd1d67f0b63d6edff21058'

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())



from github import Github
import os
from pprint import pprint
import urllib3
token ='d6a2d1c8ae3de0f86fbd1d67f0b63d6edff21058'
g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

