import uuid

from loguru import logger
from asyncpg import UniqueViolationError

from utils.db_api.schemas import User, ReplierBot, Account


async def add_user(id_: int, name: str, role: str):
    try:
        user = User(id=id_, name=name, role=role)
        await user.create()
    except UniqueViolationError:
        pass


async def add_account(user_id: int, name: str, hmac_key: str, hmac_secret: str):
    try:
        id_ = uuid.uuid4().__str__()
        account = Account(id=id_, name=name, user_id=user_id, hmac_key=hmac_key, hmac_secret=hmac_secret)
        await account.create()
    except Exception as e:
        logger.error(str(e))
