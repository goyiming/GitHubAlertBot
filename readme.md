# GitHub 监控项目

这个项目用于监控 GitHub 上的特定关键词，并将更新发送到 Telegram 群组。

## 目录结构
│
├── app.py # 主程序入口
├── config.py # 配置文件
├── database.py # 数据库操作
├── github_monitor.py # GitHub 监控逻辑
├── message_sender.py # Telegram 消息发送
├── requirements.txt # 项目依赖
└── README.md # 项目说明文档

## 功能特点

1. 监听指定的 GitHub 关键词
2. 自定义检测频率
3. 自定义发送频率
4. 可配置关键词列表
5. 可选择是否启用代理
6. 将更新发送到 Telegram 群组
7. 通过命令行查询统计信息和详细信息

## 使用方法

1. 安装依赖：   ```
   pip install -r requirements.txt   ```

2. 配置 `config.py` 文件：
   - 设置 Telegram Bot Token
   - 设置 Telegram 群组 ID
   - 配置 GitHub 访问令牌（可选，用于增加 API 限制）
   - 设置关键词列表
   - 配置检测频率和发送频率
   - 设置代理选项

3. 运行程序：
   - 启动监控：`python app.py`
   - 查看基本统计信息：`python app.py --stats`
   - 查看详细统计信息：`python app.py --detailed`

## 配置说明

在 `config.py` 文件中，您可以自定义以下选项：

- `GITHUB_TOKEN`：GitHub 访问令牌（可选）
  获取方法：
  1. 登录您的 GitHub 账户
  2. 点击右上角的头像，选择 "Settings"
  3. 在左侧菜单中，选择 "Developer settings"
  4. 点击 "Personal access tokens"，然后选择 "Tokens (classic)"
  5. 点击 "Generate new token"，选择 "Generate new token (classic)"
  6. 为令牌命名，选择所需的权限（至少需要 `public_repo` 权限）
  7. 点击 "Generate token"，复制生成的令牌

- `TELEGRAM_BOT_TOKEN`：Telegram Bot 的访问令牌
  获取方法：
  1. 在 Telegram 中搜索 "@BotFather"
  2. 向 BotFather 发送 "/newbot" 命令
  3. 按照提示设置 bot 的名称和用户名
  4. BotFather 会提供一个 API 令牌，这就是您的 TELEGRAM_BOT_TOKEN

- `TELEGRAM_CHAT_ID`：Telegram 群组 ID
  获取方法：
  1. 将您创建的 bot 添加到目标群组
  2. 在浏览器中访问 `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
     （将 <YourBOTToken> 替换为您的 TELEGRAM_BOT_TOKEN）
  3. 在返回的 JSON 中查找 "chat" 对象，其中的 "id" 字段就是您需要的群组 ID
  4. 群组 ID 通常是一个负数，例如 -1001234567890

- `KEYWORDS`：要监控的 GitHub 关键词列表
- `CHECK_INTERVAL`：检测间隔时间（秒）
- `SEND_INTERVAL`：发送间隔时间（秒）
- `USE_PROXY`：是否使用代理（True/False）
- `PROXY_URL`：代理服务器 URL（如果启用代理）

## 注意事项

- 请确保您的 Telegram Bot 已被添加到目标群组中
- 如果频繁使用，建议设置 GitHub 访问令牌以避免 API 限制
- 合理设置检测和发送间隔，以避免对 GitHub 和 Telegram 服务器造成过大压力

## 贡献

欢迎提交 Issues 和 Pull Requests 来改进这个项目！

## 许可证

MIT License
