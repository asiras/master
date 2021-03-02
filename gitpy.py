#gitpython library abc

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
    local_folder=input('\nEnter local path to store code:')
    try:
        Repo.clone_from(repo_name,local_folder)
        print('\nRepository clonned successfully')
    except Exception as e:
        print('Could not clone')
        print(e)
#COMMIT_MESSAGE = 'comment from python script'
repo_path="D://test_git//"

COMMITS_TO_PRINT = 2

def print_diff(repo):
    diff = repo.git.diff(repo.head.commit.tree)
    print('\n\n')
    print(diff)

def print_commit_data(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))

def list_remotes(repo):
    print(' \n Remotes:')
    for remote in repo.remotes:
        print(f'- {remote.name} {remote.url}')
    #repo.delete_remote('my_new_branch')


def create_new_branch(repo):
    # List all branches
    print("\nBranches availabe are :")
    for branch in repo.branches:
        print(branch)

    # Create a new branch
    
    new_branch=input('\nEnter branch name:')
    try:
        repo.git.branch(new_branch)
        print('branch created ')
    except:
        print('branch already exists!')

    # You need to check out the branch after creating it if you want to use it
    repo.git.checkout(new_branch)
    current = repo.create_head(new_branch)
    print(repo.git.status())
    repo.git.add('.')
    repo.index.commit(input("Enter commit message : "))
    repo.git.push("--set-upstream", 'origin', current)
    #print("--->",repo.head.ref)
    print('data pushed!!')


    #To checkout master again:
    #repo.git.checkout('main')

def print_repository_info(repo):

    print('\nRepository active branch is {}'.format(repo.active_branch))

    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))

def git_push():
    try:
        repo = Repo(repo_path)
        print(repo.git.status())
        print(repo.git.pull())
        print('adding files to repo...')

        repo.git.add('.')
        repo.index.commit(input("enter commit message : "))
        origin = repo.remote(name='origin')
        origin.push()
        print('data pushed!!')
    except Exception as e:
        print(e)
        print('Some error occured while pushing the code')    


if __name__=='__main__':
    
    # Repo object used to interact with Git repositories
    repo = Repo(repo_path)
    #clone()

    #print_diff(repo)# print changes made to file 

    #list_remotes(repo)
    

    #check that the repository loaded correctly
    # if not repo.bare:
    #     print('\n Repo at {} successfully loaded.'.format(repo_path))
    #     print_repository_info(repo)

    #     ## create list of commits then print some of them to stdout
    #     # commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
    #     # for commit in commits:
    #     #     print_commit_data(commit)
    #     #     pass

    # else:
    #     print('Could not load repository at {} :'.format(repo_path))
    
    create_new_branch(repo)#create new branch
    #git_push()
    