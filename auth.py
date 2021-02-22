# import os
# from pprint import pprint
# import requests
# token ='0af5046d5bc732cb1ca2311cd37bd164041d6d27'

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())



from github import Github
import os
from pprint import pprint
import urllib3
token ='0af5046d5bc732cb1ca2311cd37bd164041d6d27'
g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

