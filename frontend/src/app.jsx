import React, { useState } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [data, setData] = useState(null);

  const fetchProfile = async () => {
    const res = await fetch(`https://github-profile-optimizer-backend.onrender.com/api/profile/${username}`);
    const result = await res.json();
    setData(result);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 text-center">
      <h1 className="text-3xl font-bold mb-6">GitHub Profile Optimizer</h1>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Enter GitHub username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="px-4 py-2 border border-gray-300 rounded mr-2"
        />
        <button
          onClick={fetchProfile}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Analyze
        </button>
      </div>

      {data && data.profile && (
        <div className="bg-white p-6 rounded shadow-md max-w-xl mx-auto">
          <h2 className="text-xl font-semibold mb-2">{data.profile.name} ({data.profile.login})</h2>
          <img src={data.profile.avatar_url} alt="avatar" className="w-24 mx-auto rounded-full mb-4" />
          <p>Public Repos: {data.repo_stats.total_repos}</p>
          <p>Total Stars: ⭐ {data.repo_stats.total_stars}</p>
          <p>Total Forks: 🍴 {data.repo_stats.total_forks}</p>
          <p className="mt-2 font-medium">Top Languages:</p>
          <ul>
            {data.repo_stats.top_languages.map(([lang, count]) => (
              <li key={lang}>{lang} ({count})</li>
            ))}
          </ul>
          {data.repo_stats.top_repo && (
            <div className="mt-4">
              <p className="font-medium">Top Repo:</p>
              <a
                href={data.repo_stats.top_repo.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 underline"
              >
                {data.repo_stats.top_repo.name} ⭐ ({data.repo_stats.top_repo.stars})
              </a>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
