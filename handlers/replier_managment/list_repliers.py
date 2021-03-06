from aiogram.types import CallbackQuery

from keyboards.repliers import user_accounts_markup


async def list_replier_accounts(callback: CallbackQuery):
    user_id = callback.from_user.id
    markup = await user_accounts_markup(user_id)
    await callback.message.edit_text("Аккаунты")
    await callback.message.edit_reply_markup(markup)
