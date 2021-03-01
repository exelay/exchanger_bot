from loguru import logger
from localbitcoins_sdk import LBClient

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from loader import dp
from states import AccountData
from utils.db_api.quick_commands import add_account
from utils.db_api.schemas import Account
from keyboards.cancel_buttons import cancel_markup


@dp.callback_query_handler(text='add_account')
async def add_account_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    text = (
        "Укажите имя аккаунта\n"
        "(имя должно быть уникальным, оно предназначено для поиска нужного аккаунта в БД):"
    )
    await dp.bot.send_message(user_id, text, reply_markup=cancel_markup)
    await AccountData.name.set()


@dp.message_handler(state=AccountData.name)
async def get_account_name(message: Message, state: FSMContext):
    if await name_is_free(message.text, message.from_user.id):
        await state.update_data(name=message.text)
        await message.answer("Ваш HMAC KEY:", reply_markup=cancel_markup)
        await AccountData.next()
    else:
        text = "Аккаунт с таким именем уже привязан\nВыберете другое имя или проверьте привязанные аккаунты."
        await message.answer(text, reply_markup=cancel_markup)


@dp.message_handler(state=AccountData.hmac_key)
async def get_hmac_key(message: Message, state: FSMContext):
    await state.update_data(hmac_key=message.text)
    await message.answer("Ваш HMAC SECRET:", reply_markup=cancel_markup)
    await AccountData.next()


@dp.message_handler(state=AccountData.hmac_secret)
async def get_hmac_secret(message: Message, state: FSMContext):
    await state.update_data(hmac_secret=message.text)
    user_id = message.from_user.id
    data = await state.get_data()

    if await account_is_valid(data):

        await add_account(
            user_id=user_id,
            name=data['name'],
            hmac_key=data['hmac_key'],
            hmac_secret=data['hmac_secret']
        )
        await message.answer("Аккаунт успешно привязан")
    else:
        await message.answer("Не удалось привязать аккаунт. Проверьте правильность ключей и попробуйте заново.")
    await state.finish()


async def name_is_free(name, user_id) -> bool:
    account = await Account.query.where(Account.name == name and Account.user_id == user_id).gino.first()
    if account:
        return False
    else:
        return True


async def account_is_valid(data):
    client = LBClient(data['hmac_key'], data['hmac_secret'])
    try:
        client.get_myself()
        return True
    except Exception as e:
        logger.error(f"Can't get data about account: {e}")
        return False
