# GitHub 配置
GITHUB_TOKEN = "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"  # 可选，用于增加 API 限制

# Telegram 配置
TELEGRAM_BOT_TOKEN = "XXXXXXXXXX:XXXXXXX-_XXXXXXXXXXXXX-XXXXXXX-XXXX"
TELEGRAM_CHAT_ID = -XXXXXXXXXXXXX  # 修改为整数类型 一般群组ID前面有一个减号

# 监控配置
KEYWORDS = ["漏洞", "CVE", "安全"]
CHECK_INTERVAL = 600  # 每600秒检查一次
SEND_INTERVAL = 610  # 每610秒发送一次

# 代理配置
USE_PROXY = True    如果不开启代理可改为False，主要是为了解决大陆无法访问github问题
PROXY_URL = "http://127.0.0.1:10090"

