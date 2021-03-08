from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from loader import dp
from states import ReplierData
from keyboards.cancel_buttons import cancel_markup
from keyboards.repliers import repliers_cd, user_accounts_markup, creating_actions_markup
from keyboards.menu import categories_keyboard
from utils.db_api.quick_commands import add_replier


async def create_replier(callback: CallbackQuery):
    user_id = callback.from_user.id
    markup = await user_accounts_markup(user_id)
    await callback.message.edit_text("👇 На каком аккаунте создать автоответчик?")
    await callback.message.edit_reply_markup(markup)
    await ReplierData.account.set()


@dp.callback_query_handler(repliers_cd.filter(), state=ReplierData.account)
async def navigate(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    current_level = callback_data.get('level')
    account = callback_data.get('account')

    levels = {
        '1': start_creating,
    }
    current_level_function = levels.get(current_level)
    try:
        await current_level_function(
            callback,
            account,
            state,
        )
    except TypeError:
        pass


async def start_creating(callback: CallbackQuery, account, state):
    await callback.message.edit_text(
        "Дайте имя автоответчику (По нему ты будешь его идентифицировать)"
    )
    await callback.message.edit_reply_markup(cancel_markup)
    await state.update_data(account_name=account)
    await ReplierData.name.set()


@dp.message_handler(state=ReplierData.name)
async def get_replier_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Укажите реквизиты, которые будут показаны пользователю.", reply_markup=cancel_markup)
    await ReplierData.next()


@dp.message_handler(state=ReplierData.payment_info)
async def get_payment_info(message: Message, state: FSMContext):
    await state.update_data(payment_info=message.text)
    markup = await creating_actions_markup()
    await message.answer("Что сделать?", reply_markup=markup)


# TODO сделать так чтобы статус «запущен» мог быть только у одного автоответчика
@dp.callback_query_handler(text=['create_and_run', 'create_and_no_run'], state=ReplierData.payment_info)
async def get_initial_status(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data['user_id'] = callback.from_user.id
    if callback.data == 'create_and_run':
        text = "Автоответчик создан и запущен!"
        data['working'] = True
    else:
        text = "Автоответчик создан!"
        data['working'] = False

    await add_replier(**data)
    markup = await categories_keyboard()
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(text)
    await callback.message.answer("⚙️ Main menu", reply_markup=markup)
    await state.finish()
