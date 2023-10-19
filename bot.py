import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()


dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start_handler(message: Message):
    await message.answer(f"Приветствую, {message.from_user.first_name}!")

@dp.message()
async def echo(message: types.Message):
    await message.reply("Я вас не понимаю(((")

async def main():
    bot = Bot(os.getenv("TOKEN_API"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())