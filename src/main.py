import os
from github import Github, Auth
from dotenv import load_dotenv

if __name__ == '__main__':

    load_dotenv()
    acces_token = os.environ.get('GITHUB_TOKEN')
    repo_uri = os.environ.get('GITHUB_REPOSITORY')
    pr_number = os.getenv('GITHUB_REF').split('/')[-1]

    if(repo_uri is None or acces_token is None):
        raise Exception('Could not find repository')
    token = Auth.Token(acces_token)

    github = Github(auth=token)
    repo = github.get_repo(repo_uri)

    pull_request = repo.get_pull(pr_number)
    commits = pull_request.get_commits()
    
    for c in commits:
        print(c.commit.message)