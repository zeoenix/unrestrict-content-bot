# TechVJ Save Content Bot 🤖

A powerful Telegram bot that allows users to save restricted content from private channels, groups, and bot chats.

---
## Support 💬

**Latest Creator:**
- 📢 Updates: [@TP_botz](https://t.me/TP_Botz)
- 💬 Support: [@TP_bot_disscussion](https://t.me/TP_Botz)
- 👨‍💻 Main Developer: [@kingvj01](https://t.me/kingvj01)

**Enhanced Version:**
- 🔧 Enhanced By: [@TP_Botz](https://t.me/TP_Botz)
- 👨‍💻 Enhanced Developer: [@TP_Botz](https://t.me/TP_Botz)
- 💬 **For Any Query (Enhanced Features):** [@TP_Botz](https://t.me/TP_Botz)
- 🛡️ Security & Production Updates Video Tutorial - [Click Here](https://youtu.be/BFEvSX5vIMg)**

---

## Features ✨

- 🔒 Save content from private Telegram channels
- 🤖 Save content from bot chats
- 📁 Batch download multiple messages
- 👤 User session management with login/logout
- 📊 Admin broadcast functionality
- 🔐 Secure session handling
- 📈 User analytics and database management

## Security Improvements 🛡️

This version includes several security enhancements:
- ✅ Environment variable validation
- ✅ Secure credential handling
- ✅ Updated dependencies to fix vulnerabilities
- ✅ Proper error handling and logging
- ✅ Input validation and sanitization
- ✅ Rate limiting implementation

## Setup Instructions 🚀

### 1. Prerequisites
- Python 3.10+
- MongoDB database
- Telegram Bot Token
- Telegram API credentials

### 2. Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Archive
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Edit `.env` file with your credentials:
```env
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
ADMINS=your_admin_user_id_here
DB_URI=your_mongodb_connection_string_here
DB_NAME=vjsavecontentbot
ERROR_MESSAGE=True
```

## Environment Variables 🔧

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Bot Token From [BotFather](https://telegram.me/BotFather) | ✅ |
| `API_ID` | Your API ID From [Telegram Website](https://my.telegram.org) | ✅ |
| `API_HASH` | Your API Hash From [Telegram Website](https://my.telegram.org) | ✅ |
| `ADMINS` | Your Admin User ID For Broadcasting Messages | ✅ |
| `DB_URI` | Your MongoDB Database URL From [MongoDB](https://mongodb.com) | ✅ |
| `DB_NAME` | Database Name | ❌ (default: vjsavecontentbot) |
| `ERROR_MESSAGE` | Show detailed errors (True/False) | ❌ (default: True) |

⚠️ **Warning:** Never commit your actual credentials to the repository. Always use environment variables.

## Commands 📋

- `/start` : Check if bot is working and see welcome message
- `/help` : Get help information on how to use the bot
- `/login` : Login with your Telegram account session 
- `/logout` : Logout from your current session 
- `/cancel` : Cancel any ongoing batch operation
- `/broadcast` : Broadcast message to all users (Admin Only)

## Usage 📖

### Public Chats
Just send the post link:
```
https://t.me/channel_username/123
```

### Private Chats
First send invite link of the chat (unnecessary if the account is already a member), then send post link:
```
https://t.me/c/channel_id/123
```

### Bot Chats
Send link with '/b/', bot's username and message id:
```
https://t.me/b/botusername/4321
```

### Multi Posts (Batch Download)
Send public/private post links with format "from - to" to download multiple messages:
```
https://t.me/channel_username/1001-1010
https://t.me/c/channel_id/101-120
```
Note: Spaces between numbers don't matter.

## Deployment 🚀

### Local Development
```bash
python bot.py
```

### With Flask (for deployment platforms)
```bash
python app.py & python bot.py
```

### Docker
```bash
docker build -t techvj-bot .
docker run -d --env-file .env techvj-bot
```

## Security Notes ⚠️

- **Never commit your `.env` file to version control**
- **Use strong, unique credentials**
- **Regularly update dependencies**
- **Monitor bot logs for suspicious activity**
- **Respect Telegram's Terms of Service**

## Support 💬

**Original Creator:**
- 📢 Updates: [@vj_botz](https://t.me/vj_botz)
- 💬 Support: [@vj_bot_disscussion](https://t.me/vj_bot_disscussion)
- 👨‍💻 Developer: [@kingvj01](https://t.me/kingvj01)

**Enhanced Version:**
- 🔧 Enhanced By: [@TP_Botz](https://t.me/TP_Botz)
- �‍💻 Enhanced Developer: [@TP_Botz](https://t.me/TP_Botz)
- �🛡️ Security & Production Updates

## Credits 🙏

- Thanks To [BipinKrish](https://github.com/bipinkrish) For Base Repository
- Thanks To [Tech VJ](https://telegram.dog/Kingvj01) For Modifications & Login Feature  
- **Enhanced & Modified By [TP_Botz](https://t.me/TP_Botz) - Security Improvements & Production Ready Version**

---

**⚠️ Disclaimer:** This bot is for educational purposes only. Users are responsible for complying with Telegram's Terms of Service and local laws.

**📝 License:** This project is open source. Please maintain credits when redistributing.
