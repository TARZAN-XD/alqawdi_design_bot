# bot.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import register_handlers
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    await set_bot_commands()
    register_handlers(dp)
    await dp.start_polling(bot)

async def set_bot_commands():
    commands = [
        BotCommand(command="start", description="ابدأ البوت"),
        BotCommand(command="help", description="مساعدة")
    ]
    await bot.set_my_commands(commands)

if __name__ == "__main__":
    asyncio.run(main())
