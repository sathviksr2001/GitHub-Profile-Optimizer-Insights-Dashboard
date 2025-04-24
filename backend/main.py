# backend/main.py

# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from github_api import get_full_profile_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GitHub Profile Optimizer API is running!"}

@app.get("/api/profile/{username}")
def get_profile(username: str):
    return get_full_profile_summary(username)
