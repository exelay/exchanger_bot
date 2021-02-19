from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
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
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    feature_id = callback_data.get("item_id")

    levels = {
        "0": list_categories,
        "1": list_subcategories,
    }
    current_level_function = levels[current_level]
    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        feature_id=feature_id
    )
