from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from messages import MESSAGES

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def help_command(message: types.Message):
    await message.answer(MESSAGES['help'])
