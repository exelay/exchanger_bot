from sqlalchemy import BigInteger, String, Column, Boolean, sql

from utils.db_api.db_gino import db, TimedBaseModel


class ReplierBot(TimedBaseModel):

    __tablename__ = 'replier_bots'

    name = Column(String(255), primary_key=True)
    user_id = Column(BigInteger, db.ForeignKey('users.id'))
    payment_info = Column(String(1000))
    working = Column(Boolean())
    account_name = Column(String(255), db.ForeignKey('accounts.name'))

    query: sql.Select
