from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from states import AccountData, ReplierData
from handlers.basic.menu import list_categories


states = [
    AccountData.name,
    AccountData.hmac_key,
    AccountData.hmac_secret,
    ReplierData.account,
    ReplierData.name,
    ReplierData.payment_info,
]


@dp.callback_query_handler(text='cancel_adding',
                           state=states)
async def cancel_adding(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    await list_categories(callback)
