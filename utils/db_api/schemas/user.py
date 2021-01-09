from sqlalchemy import BigInteger, String, Column, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    role = Column(String(100))

    query: sql.Select
