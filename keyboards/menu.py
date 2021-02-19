from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


menu_cd = CallbackData("show_menu", "level", "category", "subcategory")

categories = (
    ('accounts', '🎛 Аккаунты'),
    ('replier', '📼 Автоответчик'),
    ('ad_manager', '📈 Менеджер объявлений'),
)

subcategories = {
    'accounts': (
        ('my_accounts', '📜 Мои аккаунты'),
        ('add_account', '🔗 Привязать аккаунт'),
        ('remove_account', '✂️ Отвязать аккаунт'),
        ('update_account', '📝 Обновить ключи'),
    ),
    'replier': (
        ('reply_msg', '✍️ Изменить ответ'),
        ('turn_on', '🟢 Включить'),
        ('turn_off', '🔴 Выключить')
    ),
    'ad_manager': (
        ('create', '🪄 Создать'),
        ('delete', '💣 Удалить'),
        ('list', '📋 Список'),
        ('turn_on', '🟢 Включить'),
        ('turn_off', '🔴 Выключить')
    )
}


def make_callback_data(level, category="0", subcategory="0"):
    return menu_cd.new(level=level, category=category, subcategory=subcategory)


async def categories_keyboard():
    current_level = 0

    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(text='🔗 Привязать аккаунт', callback_data='add_account')
    )
    for category, text in categories:
        callback_data = make_callback_data(level=current_level + 1, category=category)
        markup.insert(
            InlineKeyboardButton(text=text, callback_data=callback_data)
        )
    return markup


async def subcategories_keyboard(category):
    current_level = 1
    markup = InlineKeyboardMarkup(row_width=2)

    try:
        for subcategory, text in subcategories[category]:
            callback_data = make_callback_data(level=current_level + 1,
                                               category=category, subcategory=subcategory)
            markup.insert(
                InlineKeyboardButton(text=text, callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="Назад",
                callback_data=make_callback_data(level=current_level - 1))
        )
    except KeyError:
        pass
    return markup
