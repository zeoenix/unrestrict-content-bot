#!/usr/bin/env python3
"""
Configuration validation script
Run this before starting the bot to ensure all required environment variables are set
"""

import os
import sys
import logging
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def validate_config():
    """Validate all required configuration variables"""
    errors = []
    warnings = []
    
    # Required variables
    required_vars = {
        'BOT_TOKEN': 'Telegram Bot Token',
        'API_ID': 'Telegram API ID',
        'API_HASH': 'Telegram API Hash', 
        'ADMINS': 'Admin User ID',
        'DB_URI': 'MongoDB Connection String'
    }
    
    print("🔍 Validating configuration...")
    print("-" * 50)
    
    # Check required variables
    for var, description in required_vars.items():
        value = os.environ.get(var)
        if not value:
            errors.append(f"❌ {var} ({description}) is not set")
        else:
            print(f"✅ {var}: {'*' * (len(str(value)) - 4) + str(value)[-4:]}")
    
    # Validate specific formats
    api_id_str = os.environ.get('API_ID')
    if api_id_str:
        try:
            api_id = int(api_id_str)
            if api_id <= 0:
                errors.append("❌ API_ID must be a positive integer")
        except ValueError:
            errors.append("❌ API_ID must be a valid integer")
    
    admin_id_str = os.environ.get('ADMINS')
    if admin_id_str:
        try:
            admin_id = int(admin_id_str)
            if admin_id <= 0:
                errors.append("❌ ADMINS must be a positive integer")
        except ValueError:
            errors.append("❌ ADMINS must be a valid integer")
    
    # Validate bot token format
    bot_token = os.environ.get('BOT_TOKEN')
    if bot_token and ':' not in bot_token:
        errors.append("❌ BOT_TOKEN format appears invalid (should contain ':')")
    
    # Validate MongoDB URI
    db_uri = os.environ.get('DB_URI')
    if db_uri:
        try:
            parsed = urlparse(db_uri)
            if not parsed.scheme.startswith('mongodb'):
                warnings.append("⚠️  DB_URI should start with 'mongodb://' or 'mongodb+srv://'")
        except Exception:
            errors.append("❌ DB_URI format appears invalid")
    
    # Optional variables
    optional_vars = {
        'DB_NAME': os.environ.get('DB_NAME', 'vjsavecontentbot'),
        'ERROR_MESSAGE': os.environ.get('ERROR_MESSAGE', 'True')
    }
    
    print("\n📋 Optional Configuration:")
    for var, value in optional_vars.items():
        print(f"   {var}: {value}")
    
    # Print results
    print("\n" + "=" * 50)
    
    if warnings:
        print("⚠️  Warnings:")
        for warning in warnings:
            print(f"   {warning}")
        print()
    
    if errors:
        print("❌ Configuration Errors:")
        for error in errors:
            print(f"   {error}")
        print(f"\n💡 Please set the missing environment variables and try again.")
        print("   You can copy .env.example to .env and fill in your values.")
        return False
    else:
        print("✅ All required configuration is valid!")
        print("🚀 Ready to start the bot!")
        return True

if __name__ == "__main__":
    if not validate_config():
        sys.exit(1)
    print("\n🎉 Configuration validation passed!")
