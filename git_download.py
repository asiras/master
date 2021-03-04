#gitpython library

from github import Github
from getpass import getpass
from git import Repo
import os
import sys
username=input('enter your user name:')
access_token =getpass('Personal Access Token:')
g = Github(access_token)

try:
    repo_list = [i for i in g.get_user().get_repos()]
    print('\n')
    for i in repo_list:
        repo_name = str(i).replace('Repository(full_name="', '')
        repo_name = str(repo_name).replace('")', '')
        print('https://github.com/' + repo_name)
except Exception as e:
    print('\nCredientials does not match')
    print(e)
    sys.exit()

def clone():
    repo_name=input('\nEnter repository link to be cloned:')
    local_folder=input('\nEnter local path to clone files:')
    try:
        Repo.clone_from(repo_name,local_folder)
        print('\nRepository cloned successfully')
    except Exception as e:
        print('Could not clone')
        print(e)
    
if __name__=='__main__':
    clone()

    