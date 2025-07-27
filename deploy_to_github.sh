#!/bin/bash

echo "🚀 Deploying TechVJ Bot to GitHub..."
echo "📋 Credits: Original by @VJ_Botz | Enhanced by @TP_Botz"

# Check if we're in the right directory
if [ ! -f "bot.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
fi

# Add all files
echo "📁 Adding files to Git..."
git add .

# Show what will be committed (excluding ignored files)
echo "📋 Files to be committed:"
git status --short

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "TechVJ Save Content Bot - Enhanced Version

Original Credits:
- Base: BipinKrish  
- Main Developer: @VJ_Botz (Tech VJ)
- YouTube: https://youtube.com/@Tech_VJ

Enhanced By: @TP_Botz
- Security improvements applied
- Dependencies updated to fix vulnerabilities  
- Production-ready configuration
- Enhanced error handling & logging
- Virtual environment setup
- Deployment automation

Features:
- Telegram content downloader
- Flask web interface  
- MongoDB integration
- Login/logout system
- Admin broadcast functionality
- Batch download support"

echo "✅ Git repository prepared!"
echo ""
echo "🌐 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Run these commands with your GitHub repo URL:"
echo ""
echo "git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
echo "git branch -M main" 
echo "git push -u origin main"
echo ""
echo "🔒 Security note: Your .env file with secrets is safely ignored"
echo "📋 Credits maintained: @VJ_Botz (Original) | @TP_Botz (Enhanced)"
echo "🔗 Developer Links:"
echo "   Original: https://t.me/kingvj01"
echo "   Enhanced: https://t.me/TP_Botz"
