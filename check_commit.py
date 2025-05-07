import requests
import json

# Configuration
REPO = "minnathdhani/ci-cd_pipeline-hvp"
BRANCH = "master"
TOKEN = "ghp_YourGitHubToken"
LOCAL_FILE = "/home/ubuntu/last_commit.txt"

def get_latest_commit():
    url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()["sha"]

def read_last_commit():
    try:
        with open(LOCAL_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def write_last_commit(sha):
    with open(LOCAL_FILE, 'w') as f:
        f.write(sha)

if __name__ == "__main__":
    latest = get_latest_commit()
    previous = read_last_commit()
    if latest != previous:
        print("New commit found. Deploying...")
        write_last_commit(latest)
        import subprocess
        subprocess.run(["/bin/bash", "/home/ubuntu/deploy.sh"])
    else:
        print("No new commits.")
