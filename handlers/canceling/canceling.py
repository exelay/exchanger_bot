from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from states import AccountData
from handlers.basic.menu import list_categories


@dp.callback_query_handler(text='cancel_adding_account',
                           state=[AccountData.name, AccountData.hmac_key, AccountData.hmac_secret])
async def cancel_adding_account(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    await list_categories(callback)
