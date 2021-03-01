from aiogram.types import CallbackQuery

from loader import dp
from utils.db_api.quick_commands import delete_account
from keyboards.accounts import user_accounts_markup, delete_account_cd, selection_buttons_markup


async def disconnect_account(callback: CallbackQuery):
    user_id = callback.from_user.id
    markup = await user_accounts_markup(user_id)
    await callback.message.edit_text("Какой аккаунт отвязать?")
    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(delete_account_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    account = callback_data.get("account")
    action = callback_data.get("action")

    levels = {
        '1': show_selection_buttons,
        '2': select_action,
    }
    current_level_function = levels.get(current_level)
    try:
        await current_level_function(
            call,
            account=account,
            action=action,
        )
    except TypeError:
        pass


async def show_selection_buttons(callback: CallbackQuery, account, **kwargs):
    markup = await selection_buttons_markup(account)
    await callback.message.edit_text(f"Отвязать {account}?")
    await callback.message.edit_reply_markup(markup)


async def select_action(callback: CallbackQuery, account, action):
    if action == 'delete':
        await delete_account(account)
        await callback.answer("Аккаунт успешно отвязан!")
    elif action == 'cancel':
        await disconnect_account(callback)
