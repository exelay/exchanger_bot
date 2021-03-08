from aiogram.dispatcher.filters.state import StatesGroup, State


class ReplierData(StatesGroup):
    account = State()
    name = State()
    payment_info = State()
