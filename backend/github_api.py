# backend/github_api.py

import requests

def fetch_github_profile(username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found or rate-limited"}
