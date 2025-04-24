
# GitHub Profile Optimizer

This project allows users to analyze and optimize their GitHub profiles. The app provides valuable insights into a GitHub profile, such as:

- **Total Repositories**
- **Total Stars**
- **Total Forks**
- **Top Programming Languages**
- **Top Repositories by Stars**

It includes a **frontend** built using **React** and **TailwindCSS** and a **backend** built with **FastAPI**.

## Features

- **Frontend**:
  - GitHub profile data input
  - Display of profile stats such as total repos, stars, forks, and top languages
  - Ability to display the top repo based on stars

- **Backend**:
  - FastAPI service to fetch profile data from GitHub API
  - Calculation of repository stats (total stars, forks, etc.)
  - Integration with a third-party API to fetch repository data

---

## Prerequisites

Before you begin, ensure you have the following tools installed:

- **Node.js** (for frontend)
- **Python 3.9+** (for backend)
- **Git** (for version control)
- **Vercel** (for frontend deployment)
- **Render** (for backend deployment)

---

## Project Structure

```
github-profile-optimizer/
│
├── frontend/                              # React frontend code
│   ├── public/                            # Public files
│   ├── src/                               # React source code
│   ├── tailwind.config.js                 # Tailwind CSS configuration
│   ├── package.json                       # Frontend dependencies
│   ├── .gitignore                         # Git ignore for frontend
│   └── README.md                          # Frontend project information
│
└── backend/                               # FastAPI backend code
    ├── app/
    │   ├── main.py                        # FastAPI app definition
    │   ├── api/
    │   │   └── profile.py                 # API endpoints for profile analysis
    │   ├── requirements.txt               # Backend dependencies
    │   ├── .gitignore                     # Git ignore for backend
    │   └── README.md                      # Backend project information
```

---

## 🚀 Frontend Setup (React + TailwindCSS)

### 1. Clone the Frontend Repo

```bash
git clone https://github.com/sathviksr2001/github-profile-optimizer-frontend.git
```

### 2. Install Dependencies

Navigate into the frontend directory and install the dependencies:

```bash
cd github-profile-optimizer-frontend
npm install
```

### 3. TailwindCSS Setup

- Ensure that the **`tailwind.config.js`** and **`postcss.config.js`** files are set up correctly.
- Add the following to **`tailwind.config.js`**:

```js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

- Make sure **`src/index.css`** includes Tailwind's utility classes:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 4. Running the Frontend Locally

To run the React app locally, use the following command:

```bash
npm start
```

By default, the app will be available at **`http://localhost:3000`**.

### 5. Frontend Deployment (Vercel)

1. Go to [Vercel](https://vercel.com).
2. Create a new project and link your GitHub account.
3. Select your frontend repository (`github-profile-optimizer-frontend`).
4. Vercel will automatically detect the React app and deploy it.

Once deployed, Vercel will provide a live URL for your frontend.

---

## 🖥️ Backend Setup (FastAPI)

### 1. Clone the Backend Repo

```bash
git clone https://github.com/sathviksr2001/github-profile-optimizer-backend.git
```

### 2. Install Dependencies

Navigate into the backend directory and install the Python dependencies:

```bash
cd github-profile-optimizer-backend
pip install -r requirements.txt
```

### 3. Running the Backend Locally

To run the FastAPI app locally, use the following command:

```bash
uvicorn app.main:app --reload
```

By default, the app will be available at **`http://localhost:8000`**.

### 4. Backend Deployment (Render)

1. Go to [Render](https://render.com).
2. Create a new web service and select your backend repository (`github-profile-optimizer-backend`).
3. Select **Python** as the environment.
4. For the **Build Command**, use:

```bash
pip install -r requirements.txt
```

5. For the **Start Command**, use:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

6. Once the deployment is successful, Render will provide a live URL for your backend.

---

## 🌐 Connect Frontend and Backend

1. In the **frontend** code, update the API URL in **`src/App.jsx`**:

```js
const res = await fetch(`https://your-backend-url.onrender.com/api/profile/${username}`);
```

Replace `https://your-backend-url.onrender.com` with your actual Render backend URL.

---

## 🧑‍💻 API Documentation

### 1. Endpoint: `/api/profile/{username}`

**GET** request to fetch GitHub profile data for the given username.

#### Request:

```
GET https://your-backend-url.onrender.com/api/profile/{username}
```

#### Response:

```json
{
  "profile": {
    "login": "username",
    "name": "User Name",
    "avatar_url": "https://example.com/avatar.jpg"
  },
  "repo_stats": {
    "total_repos": 20,
    "total_stars": 1500,
    "total_forks": 120,
    "top_languages": [
      ["Python", 12],
      ["JavaScript", 8]
    ],
    "top_repo": {
      "name": "Awesome-Project",
      "url": "https://github.com/username/Awesome-Project",
      "stars": 500
    }
  }
}
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📄 Troubleshooting

- **Frontend not loading**: Make sure all dependencies are installed (`npm install`) and check the `npm start` output for errors.
- **Backend issues**: Check if the FastAPI app is running and the correct Python version is being used.
- **CORS issues**: If you face CORS errors, ensure your backend allows requests from your frontend's domain.

---

## 👨‍💻 Contributors

- **Sathvik S.R.** - Initial work, design, development
