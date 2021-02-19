from sqlalchemy import BigInteger, String, Column, sql

from utils.db_api.db_gino import db, TimedBaseModel


class ReplierBot(TimedBaseModel):

    __tablename__ = 'replier_bots'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, db.Foreign_key('users.id'))
    reply_message = Column(String(1000))
    status = Column(String(100))
    account_id = Column(String(255), db.Foreign_key('connected_sites.id'))

    query: sql.Select
