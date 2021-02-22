#gitpython library abc
from git import Repo

#Repo.clone_from("https://github.com/asiras/master.git", "D://test_git//")
import os
COMMIT_MESSAGE = 'comment from python script'
repo_path="D://test_git//"

from getpass import getpass
COMMITS_TO_PRINT = 5

def print_commit_data(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))


def print_repository_info(repo):
    print('Repository description: {}'.format(repo.description))
    print('Repository active branch is {}'.format(repo.active_branch))

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
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print('data pushed!!')
    except Exception as e:
        print(e)
        print('Some error occured while pushing the code')    


# project_dir = os.path.dirname(os.path.abspath(__file__))
# os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
# os.environ['GIT_USERNAME'] = input('enter user name ')
# os.environ['GIT_PASSWORD'] = getpass()
repo = Repo(repo_path)
# print(repo.git.pull())

print(repo.git.remote('-v'))

# import requests
# username = input("Enter the github username:")
# request = requests.get('https://api.github.com/users/'+username+'/repos')
# json = request.json()
# for i in range(0,len(json)):
#   print("Project Number:",i+1)
#   print("Project Name:",json[i]['name'])
#   print("Project URL:",json[i]['svn_url'],"\n")

if __name__=='__main__':
    
    # # Repo object used to interact with Git repositories
    # repo = Repo(repo_path)

    # #check that the repository loaded correctly
    # if not repo.bare:
    #     print('Repo at {} successfully loaded.'.format(repo_path))
    #     print_repository_info(repo)

    #     # create list of commits then print some of them to stdout
    #     commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
    #     for commit in commits:
    #         print_commit_data(commit)
    #         pass

    # else:
    #     print('Could not load repository at {} :'.format(repo_path))

    git_push()