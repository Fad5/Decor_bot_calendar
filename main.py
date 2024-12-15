import time

from aiogram import Bot, Dispatcher
import asyncio
from dotenv import find_dotenv, load_dotenv
import os

from handler_user.user import router
from hendler_csv.csv_file_download import create_cvs_file

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_router(router=router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

while True:
    create_cvs_file()
    asyncio.run(main())
