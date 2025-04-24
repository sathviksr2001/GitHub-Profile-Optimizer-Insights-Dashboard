# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from github_api import fetch_github_profile

app = FastAPI()

# Allow CORS for frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GitHub Profile Optimizer API is running!"}

@app.get("/api/profile/{username}")
def get_profile(username: str):
    return fetch_github_profile(username)
