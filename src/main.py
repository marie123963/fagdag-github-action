import os
from github import Github, Auth
#from dotenv import load_dotenv

if __name__ == '__main__':

    #load_dotenv()
    acces_token = os.environ.get('GITHUB_TOKEN')
    repo_uri = os.environ.get('GITHUB_REPOSITORY')
    pr_number = int(os.environ.get('PR_NUMBER'))

    if(repo_uri is None or acces_token is None):
        raise Exception('Could not find repository')
    token = Auth.Token(acces_token)

    github = Github(auth=token)
    repo = github.get_repo(repo_uri)

    pull_request = repo.get_pull(pr_number)
    
    def get_latest_message():
        commits_messages = [c.commit.message for c in pull_request.get_commits()]
        if (len(commits_messages) > 0) :
            return commits_messages[-1]
        else:
            return ""
        
    latest = get_latest_message()
    if latest:
        pull_request.create_issue_comment(f"💅{latest}💅")