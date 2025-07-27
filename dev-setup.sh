#!/bin/bash

# Quick development setup script
# This script activates the virtual environment and provides helpful commands

echo "🔧 TechVJ Bot Development Environment"
echo "====================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created!"
fi

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies if needed
if [ ! -f "venv/.installed" ]; then
    echo "📚 Installing dependencies..."
    pip install -r requirements.txt
    touch venv/.installed
    echo "✅ Dependencies installed!"
fi

echo ""
echo "🎉 Development environment ready!"
echo ""
echo "Available commands:"
echo "  python validate_config.py  - Validate configuration"
echo "  python bot.py              - Run the bot"
echo "  python app.py              - Run Flask web server"
echo "  ./start.sh                 - Start with validation"
echo "  ./start.sh dev             - Development mode"
echo "  ./start.sh with-flask      - Start with Flask"
echo ""
echo "📝 Don't forget to set up your .env file!"
echo "   cp .env.example .env"
echo ""

# Start a new shell with the virtual environment activated
exec $SHELL
