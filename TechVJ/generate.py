# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import traceback
import logging
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from config import API_ID, API_HASH, SESSION_STRING_SIZE
from database.db import db

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["logout"]))
async def logout(client, message):
    try:
        user_data = await db.get_session(message.from_user.id)  
        if user_data is None:
            await message.reply("**You are not logged in.**")
            return 
        
        success = await db.set_session(message.from_user.id, session=None)
        if success:
            await message.reply("**Logout Successfully** ✅")
            logger.info(f"User {message.from_user.id} logged out successfully")
        else:
            await message.reply("**Error occurred during logout. Please try again.**")
    except Exception as e:
        logger.error(f"Error in logout for user {message.from_user.id}: {e}")
        await message.reply("**An error occurred. Please try again later.**")

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["login"]))
async def main(bot: Client, message: Message):
    try:
        user_data = await db.get_session(message.from_user.id)
        if user_data is not None:
            await message.reply("**You are already logged in. First /logout your old session, then do login.**")
            return 
        
        user_id = int(message.from_user.id)
        
        # Ask for phone number
        phone_number_msg = await bot.ask(
            chat_id=user_id, 
            text="<b>Please send your phone number including country code</b>\n"
                 "<b>Example:</b> <code>+13124562345, +9171828181889</code>\n\n"
                 "Send /cancel to cancel the process.",
            timeout=300
        )
        
        if phone_number_msg.text == '/cancel':
            return await phone_number_msg.reply('<b>Process cancelled!</b>')
        
        phone_number = phone_number_msg.text.strip()
        
        # Validate phone number format
        if not phone_number.startswith('+') or len(phone_number) < 10:
            return await phone_number_msg.reply('<b>Invalid phone number format. Please include country code (e.g., +1234567890)</b>')
        
        client = Client(":memory:", API_ID, API_HASH)
        await client.connect()
        await phone_number_msg.reply("Sending OTP...")
        
        try:
            code = await client.send_code(phone_number)
        except PhoneNumberInvalid:
            await phone_number_msg.reply('**Phone number is invalid.**')
            return
        except Exception as e:
            logger.error(f"Error sending code to {phone_number}: {e}")
            await phone_number_msg.reply('**Error sending OTP. Please check your phone number and try again.**')
            return
        
        # Ask for OTP
        phone_code_msg = await bot.ask(
            user_id, 
            "Please check for an OTP in your official telegram account. "
            "If you got it, send OTP here after reading the below format.\n\n"
            "If OTP is `12345`, **please send it as** `1 2 3 4 5`.\n\n"
            "**Enter /cancel to cancel the process**", 
            filters=filters.text, 
            timeout=600
        )
        
        if phone_code_msg.text == '/cancel':
            return await phone_code_msg.reply('<b>Process cancelled!</b>')
        
        try:
            phone_code = phone_code_msg.text.replace(" ", "").strip()
            if not phone_code.isdigit() or len(phone_code) != 5:
                return await phone_code_msg.reply('**Invalid OTP format. Please enter 5 digits separated by spaces.**')
            
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except PhoneCodeInvalid:
            await phone_code_msg.reply('**OTP is invalid.**')
            return
        except PhoneCodeExpired:
            await phone_code_msg.reply('**OTP is expired.**')
            return
        except SessionPasswordNeeded:
            two_step_msg = await bot.ask(
                user_id, 
                '**Your account has enabled two-step verification. Please provide the password.**\n\n'
                '**Enter /cancel to cancel the process**', 
                filters=filters.text, 
                timeout=300
            )
            
            if two_step_msg.text == '/cancel':
                return await two_step_msg.reply('<b>Process cancelled!</b>')
            
            try:
                password = two_step_msg.text
                await client.check_password(password=password)
            except PasswordHashInvalid:
                await two_step_msg.reply('**Invalid Password Provided**')
                return
        except Exception as e:
            logger.error(f"Error during sign in for user {user_id}: {e}")
            await phone_code_msg.reply('**Error during authentication. Please try again.**')
            return
        
        try:
            string_session = await client.export_session_string()
            await client.disconnect()
            
            if len(string_session) < SESSION_STRING_SIZE:
                return await message.reply('<b>Invalid session string generated. Please try again.</b>')
            
            # Test the session string
            test_client = Client(":memory:", session_string=string_session, api_id=API_ID, api_hash=API_HASH)
            await test_client.connect()
            await test_client.disconnect()
            
            success = await db.set_session(message.from_user.id, session=string_session)
            if success:
                await bot.send_message(
                    message.from_user.id, 
                    "<b>Account login successful! ✅</b>\n\n"
                    "If you get any error related to AUTH KEY, then /logout first and /login again.\n\n"
                    "💻 Bot by @VJ_Botz | Enhanced by @TP_Botz"
                )
                logger.info(f"User {message.from_user.id} logged in successfully")
            else:
                await message.reply("**Error saving session. Please try again.**")
                
        except Exception as e:
            logger.error(f"Error in session handling for user {user_id}: {e}")
            return await message.reply_text(f"<b>ERROR IN LOGIN:</b> Please try again later.")
            
    except TimeoutError:
        await message.reply("**Timeout! Please try again with /login command.**")
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
# 
# Enhanced & Modified By - @TP_Botz
# Security Improvements & Production Ready Version
