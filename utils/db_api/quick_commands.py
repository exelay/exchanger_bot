from asyncpg import UniqueViolationError

from utils.db_api.schemas import User, ReplierBot


async def add_user(id_: int, name: str, role: str):
    try:
        user = User(id=id_, name=name, role=role)
        replier_bot = ReplierBot(id=id_, working=False)
        await user.create()
        await replier_bot.create()
    except UniqueViolationError:
        pass
