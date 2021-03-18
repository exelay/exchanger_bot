from loguru import logger

from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify

    logger.info("Connecting to Database...")
    await db_gino.on_startup()
    logger.info("Successfully connected.")

    logger.info("Creating sheets...")
    await db.gino.create_all()
    logger.info("Successfully created.")

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    logger.info("Bot has been started")
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
