#!/bin/bash

# TechVJ Bot Startup Script
# This script validates configuration and starts the bot safely

echo "🚀 Starting TechVJ Save Content Bot..."
echo "=================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Validate configuration
echo "🔍 Validating configuration..."
if ! python validate_config.py; then
    echo "❌ Configuration validation failed. Please fix the issues above."
    exit 1
fi

echo ""
echo "✅ Configuration is valid!"
echo "🔄 Starting bot..."

# Start the bot with proper error handling
if [ "$1" == "dev" ]; then
    echo "🛠️  Starting in development mode..."
    python bot.py
elif [ "$1" == "with-flask" ]; then
    echo "🌐 Starting with Flask web server..."
    python app.py &
    FLASK_PID=$!
    python bot.py &
    BOT_PID=$!
    
    # Wait for both processes
    wait $FLASK_PID $BOT_PID
else
    echo "🤖 Starting bot only..."
    python bot.py
fi
