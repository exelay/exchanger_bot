from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User


async def add_user(id_: int, name: str, role: str):
    try:
        user = User(id=id_, name=name, role=role)
        await user.create()
    except UniqueViolationError:
        pass
