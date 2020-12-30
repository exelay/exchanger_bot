from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from messages import MESSAGES


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer(MESSAGES['hello'])
