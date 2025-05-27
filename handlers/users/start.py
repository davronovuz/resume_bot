import asyncpg
from aiogram import types
import requests

from loader import dp,db,bot








@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    last_name=message.from_user.last_name
    first_name=message.from_user.first_name
    username=message.from_user.username
    request = requests.post("http://127.0.0.1:8000/create/",
                            data={
                                "telegram_id":telegram_id,
                                  "username":username,
                                  "last_name":last_name,
                                  "first_name":first_name,

                                  }
                            )
    if request.status_code==200:
        await message.answer(f"Assalomu aleykum {message.from_user.full_name} \n"
                             f"Botimizga xush kelibsiz. \n")



@dp.message_handler(commands="info")
async def bot_start(message: types.Message):
    request=requests.get("http://127.0.0.1:8000/info/")
    response=request.json()
    data=response["data"]

    await message.answer(data)


