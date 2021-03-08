from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


cancel_markup = InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='❌ Отмена', callback_data='cancel_adding')
    )
