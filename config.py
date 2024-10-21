# GitHub 配置
GITHUB_TOKEN = "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"  # 可选，用于增加 API 限制

# Telegram 配置
TELEGRAM_BOT_TOKEN = "7445994479:AAHz4Rb-_U7LU8zN7g4cdE-LqMDeLq-ubFo"
TELEGRAM_CHAT_ID = -1002292162960  # 修改为整数类型

# 监控配置
KEYWORDS = ["漏洞", "CVE", "安全"]
CHECK_INTERVAL = 60  # 每60秒检查一次
SEND_INTERVAL = 70  # 每70秒发送一次

# 代理配置
USE_PROXY = True
PROXY_URL = "http://127.0.0.1:10090"

# 在文件末尾添加以下行
STATS_INTERVAL = 3600  # 每小时发送一次统计信息
