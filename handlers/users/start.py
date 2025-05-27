import asyncpg
from aiogram import types
import requests

from loader import dp,db,bot








@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.answer("Bot ishga tushdi")


@dp.message_handler(commands="info")
async def bot_start(message: types.Message):
    request=requests.get("http://127.0.0.1:8000/info/")
    response=request.json()
    data=response["data"]

    await message.answer(data)


