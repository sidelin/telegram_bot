import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ContentType

from basic import get_start, get_photo, get_text
from settings import settings

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f"Бот запущен!")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f"Бот остановлен!")

async def start():
    bot = Bot(settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=["start"]))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_text, F.text == "Привет")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())