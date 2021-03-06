from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from handlers.account_management import add_account_handler, list_accounts, disconnect_account
from handlers.replier_managment import list_replier_accounts
from keyboards.menu import menu_cd, categories_keyboard, subcategories_keyboard


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await list_categories(message)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, Message):
        await message.answer("⚙️ Main menu", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text("⚙️ Main menu")
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_text("⚙️ Main menu")
    await callback.message.edit_reply_markup(markup)


async def select_action(callback: CallbackQuery, subcategory, **kwargs):
    actions = {
        'add_account': add_account_handler,
        'my_accounts': list_accounts,
        'remove_account': disconnect_account,
        'my_repliers': list_replier_accounts,
    }
    await actions[subcategory](callback)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    action = callback_data.get("action")

    levels = {
        "0": list_categories,
        "1": list_subcategories,
        "2": select_action,
    }
    current_level_function = levels.get(current_level)
    try:
        await current_level_function(
            call,
            category=category,
            subcategory=subcategory,
            action=action
        )
    except TypeError:
        pass
