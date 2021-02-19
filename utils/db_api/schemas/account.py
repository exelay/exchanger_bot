from sqlalchemy import BigInteger, String, Column, sql

from utils.db_api.db_gino import db, TimedBaseModel


class Account(TimedBaseModel):

    __tablename__ = 'accounts'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    hmac_key = Column(String(255), unique=True)
    hmac_secret = Column(String(255), unique=True)
    user_id = Column(BigInteger, db.ForeignKey('users.id'))

    query: sql.Select