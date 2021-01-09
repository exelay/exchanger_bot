from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User


async def add_user(id_: int, name: str, status: str):
    try:
        user = User(id=id_, name=name, status=status)
        await user.create()
    except UniqueViolationError:
        pass
