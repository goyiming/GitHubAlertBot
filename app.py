import time
import argparse
from github_monitor import GitHubMonitor
from message_sender import TelegramSender
from database import Database
from config import CHECK_INTERVAL, SEND_INTERVAL
from colorama import init, Fore, Style

init(autoreset=True)  # 初始化 colorama

def main():
    github_monitor = GitHubMonitor()
    telegram_sender = TelegramSender()
    
    try:
        while True:
            print(f"{Fore.CYAN}正在检查 GitHub 更新...{Style.RESET_ALL}")
            results = github_monitor.monitor()
            
            if results:
                print(f"{Fore.GREEN}找到 {len(results)} 个新的仓库更新{Style.RESET_ALL}")
                for result in results:
                    print(f"{Fore.YELLOW}正在发送更新: {result['name']}{Style.RESET_ALL}")
                    telegram_sender.send_updates([result])
            else:
                print(f"{Fore.RED}没有找到新的更新{Style.RESET_ALL}")
            
            sleep_time = min(CHECK_INTERVAL, SEND_INTERVAL)
            print(f"{Fore.MAGENTA}等待 {sleep_time} 秒后进行下一次检查...{Style.RESET_ALL}")
            time.sleep(sleep_time)
    finally:
        telegram_sender.close()

def show_statistics(detailed=False):
    db = Database()
    stats = db.get_statistics()
    print(f"{Fore.CYAN}统计信息:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}总发送消息数: {stats[0]}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}唯一仓库数: {stats[1]}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}唯一关键词数: {stats[2]}{Style.RESET_ALL}")
    
    if detailed:
        print(f"\n{Fore.CYAN}详细信息:{Style.RESET_ALL}")
        detailed_stats = db.get_detailed_statistics()
        for repo_name, keyword, sent_at in detailed_stats:
            print(f"{Fore.YELLOW}仓库: {repo_name}, 关键词: {keyword}, 发送时间: {sent_at}{Style.RESET_ALL}")
    
    db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub 监控程序")
    parser.add_argument("--stats", action="store_true", help="显示统计信息")
    parser.add_argument("--detailed", action="store_true", help="显示详细统计信息")
    args = parser.parse_args()

    if args.stats or args.detailed:
        show_statistics(detailed=args.detailed)
    else:
        main()
