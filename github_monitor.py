import requests
from datetime import datetime, timedelta
from config import GITHUB_TOKEN, KEYWORDS, USE_PROXY, PROXY_URL

class GitHubMonitor:
    def __init__(self):
        self.base_url = "https://api.github.com/search/repositories"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if GITHUB_TOKEN:
            self.headers["Authorization"] = f"token {GITHUB_TOKEN}"
        self.proxies = {"http": PROXY_URL, "https": PROXY_URL} if USE_PROXY else None

    def search_repositories(self, keyword, since):
        query = f"{keyword} created:>{since.isoformat()}"
        params = {"q": query, "sort": "updated", "order": "desc"}
        response = requests.get(self.base_url, headers=self.headers, params=params, proxies=self.proxies)
        response.raise_for_status()
        return response.json()["items"]

    def monitor(self):
        results = []
        since = datetime.utcnow() - timedelta(hours=1)  # 检查过去一小时的更新
        for keyword in KEYWORDS:
            repos = self.search_repositories(keyword, since)
            for repo in repos:
                results.append({
                    "keyword": keyword,
                    "name": repo["full_name"],
                    "description": repo["description"],
                    "url": repo["html_url"],
                    "created_at": repo["created_at"]
                })
        return results
