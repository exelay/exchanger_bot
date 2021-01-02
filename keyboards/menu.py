from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "feature_id")
buy_item = CallbackData("buy", "item_id")  # TODO update it

categories = (
    ('replier', '📼 Автоответчик'),
    ('ad_manager', '📈 Менеджер объявлений'),
)

subcategories = {
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


def make_callback_data(level, category="0", subcategory="0", feature_id="0"):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, feature_id=feature_id)


async def categories_keyboard():
    current_level = 0

    markup = InlineKeyboardMarkup()
    for category, text in categories:
        callback_data = make_callback_data(level=current_level + 1, category=category)
        markup.insert(
            InlineKeyboardButton(text=text, callback_data=callback_data)
        )
    return markup


async def subcategories_keyboard(category):
    current_level = 1
    markup = InlineKeyboardMarkup(row_width=2)

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
    return markup


# Создаем функцию, которая отдает клавиатуру с доступными товарами, исходя из выбранной категории и подкатегории
async def features_keyboard(category, subcategory):
    current_level = 2

    markup = InlineKeyboardMarkup()

    for feature in features:
        button_text = f""

        callback_data = make_callback_data(level=current_level + 1,
                                           category=category, subcategory=subcategory,
                                           feature_id=feature.id)
        markup.insert(
            InlineKeyboardButton(
                text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=current_level - 1,
                                             category=category))
    )
    return markup


def feature_keyboard(category, subcategory, item_id):
    current_level = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text=f"Купить",
            callback_data=buy_item.new(item_id=item_id)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=current_level - 1,
                                             category=category, subcategory=subcategory))
    )
    return markup
