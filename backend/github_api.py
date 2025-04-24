# backend/github_api.py

# backend/github_api.py

import requests
from collections import Counter

GITHUB_API_URL = "https://api.github.com"

def fetch_github_profile(username: str):
    url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found or rate-limited"}

def fetch_user_repos(username: str):
    url = f"{GITHUB_API_URL}/users/{username}/repos?per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def analyze_repo_data(repos):
    total_stars = sum(repo["stargazers_count"] for repo in repos)
    total_forks = sum(repo["forks_count"] for repo in repos)
    
    languages = [repo["language"] for repo in repos if repo["language"]]
    lang_counter = Counter(languages).most_common(3)

    top_repo = max(repos, key=lambda x: x["stargazers_count"], default={})

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "top_languages": lang_counter,
        "top_repo": {
            "name": top_repo.get("name"),
            "stars": top_repo.get("stargazers_count"),
            "url": top_repo.get("html_url")
        } if top_repo else None
    }

def get_full_profile_summary(username: str):
    profile = fetch_github_profile(username)
    repos = fetch_user_repos(username)
    analysis = analyze_repo_data(repos)
    
    return {
        "profile": profile,
        "repo_stats": analysis
    }
