from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.quick_commands import select_user_accounts, select_account_repliers, replier_is_working
from .menu import menu_cd


repliers_cd = CallbackData("repliers", "level", "account", "replier", "action")


def make_callback_data(level, account="0", replier="0", action="0"):
    return repliers_cd.new(level=level, account=account, replier=replier, action=action)


selection_buttons = (
    ("delete", "✂️ Отвязать"),
    ("cancel", "⛔️ Отмена")
)

actions = (
    ('delete', '🗑 Удалить'),
    ('turn_on', '🟢 Включить'),
    ('turn_off', '🔴 Выключить')
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
            callback_data=menu_cd.new(level=1, category="replier", subcategory="0", action="0")
        )
    )
    return markup


async def user_repliers_markup(user_id, account):
    current_level = 1

    repliers = await select_account_repliers(user_id, account)
    markup = InlineKeyboardMarkup()
    for replier in repliers:
        callback_data = make_callback_data(level=current_level + 1, account=account, replier=replier.name)
        markup.insert(
            InlineKeyboardButton(text=replier.name, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="↩️ Назад",
            callback_data=menu_cd.new(level=1, category="replier", subcategory="0", action="0")
        )
    )
    return markup


async def replier_actions_markup(user_id, account, replier):
    current_level = 2

    markup = InlineKeyboardMarkup(row_width=2)
    callback_data = make_callback_data(level=current_level + 1, account=account, replier=replier, action='delete')
    markup.insert(InlineKeyboardButton(text='🗑 Удалить', callback_data=callback_data))
    callback_data = make_callback_data(level=current_level + 1, account=account, replier=replier, action='turn_status')
    if await replier_is_working(user_id=user_id, name=replier, account=account):
        markup.insert(InlineKeyboardButton(text='🔴 Выключить', callback_data=callback_data))
    else:
        markup.insert(InlineKeyboardButton(text='🟢 Включить', callback_data=callback_data))
    markup.row(
        InlineKeyboardButton(
            text="↩️ Назад",
            callback_data=menu_cd.new(level=1, category="replier", subcategory="0", action="0")
        )
    )
    return markup


async def creating_actions_markup():
    markup = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("Создать и запустить", callback_data='create_and_run'),
        InlineKeyboardButton("Создать незапуская", callback_data='create_and_no_run'),
        InlineKeyboardButton("Отмена", callback_data='cancel_adding',)
    )
    return markup
