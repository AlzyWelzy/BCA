import requests
import json

# Your GitHub access token
access_token = ""

# Your GitHub username
username = "AlzyWelzy"

# The name of the license you want to use (e.g. "agpl-3.0")
new_license = "agpl-3.0"

# Get a list of all repositories for the user
url = f"https://api.github.com/users/{username}/repos"
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github+json",
}
response = requests.get(url, headers=headers)
repos = response.json()

# Update the license for each repository
for repo in repos:
    url = repo["url"]
    data = {
        "name": repo["name"],
        "license": new_license,
    }
    response = requests.patch(url, json=data, headers=headers)
    print(response.json())
