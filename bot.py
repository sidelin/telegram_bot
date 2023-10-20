import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

# async def start_bot(bot: Bot):
#     await bot.send_message(456618518, f"Бот запущен!")

async def stop_bot(bot: Bot):
    await bot.send_message(456618518, f"Бот остановлен!")

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}")

async def start():
    load_dotenv()
    TOKEN = os.getenv("TOKEN_API")
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())