from sqlalchemy import BigInteger, String, Column, Boolean, sql

from utils.db_api.db_gino import db, TimedBaseModel


class ReplierBot(TimedBaseModel):

    __tablename__ = 'replier_bots'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, db.ForeignKey('users.id'))
    reply_message = Column(String(1000))
    working = Column(Boolean())
    account_id = Column(String(255), db.ForeignKey('connected_sites.id'))

    query: sql.Select
