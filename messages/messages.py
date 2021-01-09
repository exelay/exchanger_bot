msg_hello = (
    "Привет, {name}!\n"
    "Если ты читаешь это сообщение, значит ты находишься в списке авторизованных пользователей.\n"
    "Этот бот поможет тебе справится с рутинными задачами, при торговле на <b>LocalBitcoins</b>\n"
    "Команда /help даст тебе больше информации, ну а если ты уже в курсе всех дел, то открывай /menu "
    "и переходи к использованию."
)
msg_not_hello = (
    "Привет, {name}!\n"
    "Мы не нашли тебя в списке авторизованных пользователей, видимо ты наткнулся на этого бота случайно, "
    "или админ забыл тебя сюда добавить, если это действительно так, то сообщи ему об этом."
)
msg_help = (
    "Как пользоваться этим ботом:\n"
    "\n"
    "<b>Команды:</b>\n"
    "/start - Авторизует тебя в боте, если ты есть в списках, больше одного раза эта команда тебе не понадобится.\n"
    "/help - Увидеть это сообщение.\n"
    "/menu - Собственно меню функций этого бота, запомни эту команду, использовать её будешь часто.\n"
    "\n"
    "<b>Функции и их описание:</b>\n"
    "\n"
    "<b>Автоответчик</b>\n"
    "Проверяет заявки на покупку и автоматически отвечает на новые заявки сообщением, "
    "которое ты укажешь в настройках автоответчика.\n"
    "\n"
    "<b>Включить/выключить</b> - тут все понятно, включает и выключает автоответчик.\n"
    "<b>Изменить ответ</b> - тоже ничего сложного, нажимаешь на эту кнопку и пишешь сообщение, "
    "которым автоответчик будет отвечать на заявки.\n"
    "\n"
    "<b>Менеджер объявлений</b>\n"
    "Управляет положением объявления в списке, регулируя стоимость продажи валюты. "
    "Ты создаёшь объявление на LocalBitcoins, затем тут в меню менеджера жмешь «Создать», пишешь id своего "
    "объявления и выбираешь место, которое объявление должно занимать. Далее бот будет регулировать стоимость, "
    "чтобы место в списке соответствовало тому, которое ты задал.\n"
    "\n"
    "<b>Список</b> - список объявлений в формате: id, текущая цена, место и статус (вкл/выкл).\n"
    "<b>Создать</b> - нажимаешь сюда, пишешь id объявления, указываешь номер желаемого места.\n"
    "<b>Удалить</b> - Жмешь сюда, задем жмешь на кнопку с id объявления, которое нужно удалить.\n"
    "<b>Вкл / Выкл</b> - Тот же принцип, что и с удалением, но включает и отключает объявления.\n"
)

MESSAGES = {
    'hello': msg_hello,
    'not_hello': msg_not_hello,
    'help': msg_help,
}
