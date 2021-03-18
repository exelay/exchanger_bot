import asyncio
import time

from localbitcoins_sdk import LBClient

from utils.db_api import db_gino
from utils.db_api.quick_commands import get_all_accounts, get_replier


async def main():
    accounts = await get_all_accounts()
    repliers = [(account.id, LBClient(account.hmac_key, account.hmac_secret)) for account in accounts]
    for account_id, client in repliers:
        notifications = client.get_notifications()
        new_offers = [
            notification for notification in notifications
            if notification['msg'].startswith('Вы получили новое предложение от') and not notification['read']
        ]
        replier = await get_replier(account_id)
        payment_info = replier.payment_info
        reply_msg = (
            "|\n"
            "Добрый день.\n"
            "Реквизиты на оплату:\n"
            f"{payment_info}\n"
            "После оплаты не забудъте чек.\n"
            "Спасибо за сделку.\n"
        )
        for offer in new_offers:
            contact_id = offer['contact_id']
            client.post_message_to_contact(contact_id, reply_msg)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db_gino.on_startup())
    while True:
        loop.run_until_complete(main())
        time.sleep(20)
