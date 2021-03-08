import logging

from aiogram import Dispatcher

from data.config import ADMINS
from utils.db_api.schemas import User


async def on_startup_notify(dp: Dispatcher):
    users = await User.query.gino.all()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"Бот Запущен, всего пользователей: {len(users)}")
        except Exception as err:
            logging.exception(err)
