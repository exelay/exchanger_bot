import asyncio
import time

from localbitcoins_sdk import LBClient
from loguru import logger

from utils.db_api import db_gino
from utils.db_api.quick_commands import get_all_accounts, get_replier


async def main():
    accounts = await get_all_accounts()
    repliers = [(account.id, LBClient(account.hmac_key, account.hmac_secret)) for account in accounts]
    for account_id, client in repliers:
        logger.debug(f"Подключен аккаунт {account_id}")
        notifications = client.get_notifications()
        new_offers = [
            notification for notification in notifications
            if notification['msg'].startswith('Вы получили новое предложение от') and not notification['read']
        ]
        replier = await get_replier(account_id)
        if replier:
            logger.debug(f"Работает автоответчик {replier.name}")
            payment_info = replier.payment_info
            reply_msg = (
                "|\n"
                "Привет!\n"
                "Одним платежом на\n\n"
                f"{payment_info}\n\n"
            )
            for offer in new_offers:
                logger.debug(f"{offer}")
                contact_id = offer['contact_id']
                offer_id = offer['id']
                client.post_message_to_contact(contact_id, reply_msg)
                client.send_request(f'/api/notifications/mark_as_read/{offer_id}/', 'post')
                logger.debug(f"Ответил на заявку {offer_id} реквизитами {payment_info}")


def run_replier():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db_gino.on_startup())
    while True:
        try:
            loop.run_until_complete(main())
            time.sleep(10)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db_gino.on_startup())
    while True:
        try:
            loop.run_until_complete(main())
            time.sleep(10)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
