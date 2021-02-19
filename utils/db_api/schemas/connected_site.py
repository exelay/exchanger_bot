from sqlalchemy import BigInteger, String, Column, sql

from utils.db_api.db_gino import db, TimedBaseModel


class ConnectedSite(TimedBaseModel):

    __tablename__ = 'connected_sites'

    id = Column(String(255), primary_key=True)
    site_name = Column(String(255))
    hmac_key = Column(String(255))
    hmac_secret = Column(String(255))
    user_id = Column(BigInteger, db.ForeignKey('users.id'))

    query: sql.Select