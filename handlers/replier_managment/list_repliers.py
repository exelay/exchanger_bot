from aiogram.types import CallbackQuery

from loader import dp
from keyboards.repliers import user_accounts_markup, user_repliers_markup, replier_actions_markup, repliers_cd
from utils.db_api.quick_commands import delete_replier as del_replier
from utils.db_api.quick_commands import turn_replier_status


async def list_replier_accounts(callback: CallbackQuery):
    user_id = callback.from_user.id
    markup = await user_accounts_markup(user_id)
    await callback.message.edit_text("Аккаунты")
    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(repliers_cd.filter())
async def navigate(callback: CallbackQuery, callback_data):
    current_level = callback_data['level']
    account = callback_data['account']
    replier = callback_data['replier']
    action = callback_data['action']
    levels = {
        '1': list_account_repliers,
        '2': show_replier_actions,
        '3': do_replier_action,
    }
    current_level_function = levels.get(current_level)
    try:
        await current_level_function(
            callback=callback,
            account=account,
            replier=replier,
            action=action,
        )
    except TypeError:
        pass


async def list_account_repliers(callback: CallbackQuery, account, **kwargs):
    user_id = callback.from_user.id
    print(callback.data)
    markup = await user_repliers_markup(user_id, account)
    await callback.message.edit_text("Автоответчики")
    await callback.message.edit_reply_markup(markup)


async def show_replier_actions(callback: CallbackQuery, account, replier, **kwargs):
    user_id = callback.from_user.id
    markup = await replier_actions_markup(user_id, account, replier)
    await callback.message.edit_text("Действия")
    await callback.message.edit_reply_markup(markup)


async def delete_replier(user_id, account, replier, **kwargs):
    await del_replier(user_id, replier, account)
    await dp.bot.send_message(user_id, "Автоответчик успешно удалён!")


async def change_replier_status(user_id, account, replier, callback: CallbackQuery):
    await turn_replier_status(user_id, replier, account)
    await show_replier_actions(callback, account, replier)


async def do_replier_action(callback: CallbackQuery, account, replier, action):
    user_id = callback.from_user.id
    actions = {
        'delete': delete_replier,
        'turn_status': change_replier_status,
    }
    print(callback.data)
    action_func = actions.get(action)
    await action_func(
        user_id,
        account,
        replier,
        callback=callback,
    )
