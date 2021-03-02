from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.quick_commands import select_user_accounts
from .menu import menu_cd


accounts_cd = CallbackData("accounts", "level", "account", "action")


def make_callback_data(level, account="0", action="0"):
    return accounts_cd.new(level=level, account=account, action=action)


selection_buttons = (
    ("delete", "✂️ Отвязать"),
    ("cancel", "⛔️ Отмена")
)


async def user_accounts_markup(user_id):
    current_level = 0

    accounts = await select_user_accounts(user_id)
    markup = InlineKeyboardMarkup()
    for account in accounts:
        callback_data = make_callback_data(level=current_level + 1, account=account.name)
        markup.insert(
            InlineKeyboardButton(text=account.name, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="↩️ Назад",
            callback_data=menu_cd.new(level=1, category="accounts", subcategory="0", action="0")
        )
    )
    return markup


async def selection_buttons_markup(account):
    current_level = 1

    markup = InlineKeyboardMarkup()
    for action, text in selection_buttons:
        callback_data = make_callback_data(level=current_level + 1, account=account, action=action)
        markup.insert(
            InlineKeyboardButton(text=text, callback_data=callback_data)
        )
    return markup
