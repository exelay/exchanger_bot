from aiogram.types import CallbackQuery

from utils.db_api.quick_commands import select_user_accounts


async def list_accounts(callback: CallbackQuery):
    user_id = callback.from_user.id
    accounts = await select_user_accounts(user_id)
    text = (
        f"🗃 Добавленные аккаунты{'':10}\n"
    )
    for account in accounts:
        created_at = f"{account.created_at:%d.%m.%Y}"
        text += f"\n📁 {account.name:10}  📅 {created_at:10}"

    await callback.answer(text, show_alert=True)
