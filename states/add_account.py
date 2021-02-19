from aiogram.dispatcher.filters.state import StatesGroup, State


class AccountData(StatesGroup):
    name = State()
    hmac_key = State()
    hmac_secret = State()
