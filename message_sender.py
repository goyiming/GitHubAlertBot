import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, USE_PROXY, PROXY_URL
from database import Database
from colorama import Fore, Style

class TelegramSender:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        self.proxies = {"http": PROXY_URL, "https": PROXY_URL} if USE_PROXY else None
        self.db = Database()

    def send_message(self, message):
        data = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(self.base_url, data=data, proxies=self.proxies)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}发送消息时出错: {e}{Style.RESET_ALL}")
            print(f"{Fore.RED}响应内容: {response.text if response else 'No response'}{Style.RESET_ALL}")
            return None

    def format_message(self, repo):
        return f"""
{Fore.CYAN}创建者:{Style.RESET_ALL} {repo['name'].split('/')[0]}
{Fore.CYAN}项目描述:{Style.RESET_ALL} {repo['description'] or '无描述'}
{Fore.CYAN}项目链接:{Style.RESET_ALL} {repo['url']}

#{repo['keyword']}
"""

    def send_updates(self, results):
        for repo in results:
            message = self.format_message(repo)
            if self.send_message(message):
                self.db.record_sent_message(repo['name'], repo['keyword'])
                print(f"{Fore.GREEN}成功发送消息: {repo['name']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}无法发送消息: {repo['name']}{Style.RESET_ALL}")

    def close(self):
        self.db.close()
