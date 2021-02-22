# import os
# from pprint import pprint
# import requests
# token ='6c7fa452564ecb2e33b359b8bcecf251d1164a35'

# headers = {'Authorization': 'token ' + token}

# login = requests.get('https://api.github.com/user', headers=headers)
# pprint(login.json())



from github import Github
import os
from pprint import pprint
import urllib3
token ='6c7fa452564ecb2e33b359b8bcecf251d1164a35'
g = Github(token)
for repo in g.get_user().get_repos():
    print(repo.name)

