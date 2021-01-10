from loguru import logger

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from messages import MESSAGES
from data.config import ALLOWED_USERS, ADMINS
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    user = message.from_user.id
    user_name = message.from_user.first_name
    user_role = "admin" if user in ADMINS else "user"

    if user in ALLOWED_USERS:
        logger.info(f"User {user}({user_name}) successfully added with role {user_role}.")
        await commands.add_user(id_=user, name=user_name, role=user_role)
        await message.answer(MESSAGES['hello'].format(name=user_name))
    else:
        logger.info(f"User {user}({user_name}) is not an allowed user")
        await message.answer(MESSAGES['not_hello'].format(name=user_name))
