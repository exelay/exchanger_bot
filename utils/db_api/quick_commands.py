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
    except UniqueViolationError:
        raise ValueError
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


async def select_user_accounts(user_id: int):
    accounts = await Account.query.where(Account.user_id == user_id).gino.all()
    return accounts


async def select_account_repliers(user_id: int, account):
    repliers = await ReplierBot.query.where(
        ReplierBot.user_id == user_id and ReplierBot.account_name == account).gino.all()
    return repliers


async def add_replier(name, user_id, payment_info, working, account_name, account_id):
    try:
        id_ = uuid.uuid4().__str__()
        replier = ReplierBot(id=id_, name=name, user_id=user_id, payment_info=payment_info,
                             working=working, account_name=account_name, account_id=account_id)
        await replier.create()
    except UniqueViolationError:
        raise ValueError
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


async def delete_replier(user_id, name, account):
    replier = await ReplierBot.query.where(
        ReplierBot.user_id == user_id and ReplierBot.name == name and ReplierBot.account_name == account
    ).gino.first()
    await replier.delete()


async def turn_replier_status(user_id, name, account):
    replier = await ReplierBot.query.where(
        ReplierBot.name == name and ReplierBot.user_id == user_id and ReplierBot.account_name == account
    ).gino.first()
    if replier.working:
        await replier.update(working=False).apply()
    else:
        working_replier = await ReplierBot.query.where(
             ReplierBot.working
        ).gino.first()
        if working_replier:
            await working_replier.update(working=False).apply()
        await replier.update(working=True).apply()


async def replier_is_working(user_id, name, account):
    replier = await ReplierBot.query.where(
        ReplierBot.name == name and ReplierBot.user_id == user_id and ReplierBot.account_name == account
    ).gino.first()
    return replier.working


async def delete_account(user_id, name: str):
    account = await Account.query.where(Account.name == name and Account.user_id == user_id).gino.first()
    await account.delete()


async def update_account_keys(user_id, name, hmac_key, hmac_secret):
    account = await Account.query.where(Account.name == name and Account.user_id == user_id).gino.first()
    account.update(hmac_key=hmac_key, hmac_secret=hmac_secret).apply()


async def get_replier(account_id):
    return await ReplierBot.query.where(ReplierBot.working == True and ReplierBot.account_id == account_id).gino.first()


async def get_account(user_id, account):
    return await Account.query.where(Account.user_id == user_id and Account.name == account).gino.first()


async def get_all_accounts():
    accounts = await Account.query.gino.all()
    return accounts
