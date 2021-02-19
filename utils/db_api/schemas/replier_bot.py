from sqlalchemy import BigInteger, String, Column, sql

from utils.db_api.db_gino import TimedBaseModel


class ReplierBot(TimedBaseModel):

    __tablename__ = 'replier_bots'

    user_id = Column(BigInteger, primary_key=True)
    reply_message = Column(String(1000))
    status = Column(String(100))
    account_id = Column(String(255))

    query: sql.Select
