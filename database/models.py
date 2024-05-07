from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    surname = Column(String, unique=True)
    phone_number = Column(String, unique=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    country = Column(String, nullable=True)
    reg_day = Column(DateTime)

class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_name = Column(String)
    card_number = Column(Integer)
    balance = Column(Float, default=0)
    exp_date = Column(Integer)

    user_fk = relationship(User, lazy='subquery')

class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, autoincrement=True, primary_key=True)
    card_from_id = Column(Integer, ForeignKey('cards.card_id'))
    card_to_id = Column(Integer)
    amount = Column(Float)

    status = Column(Boolean, default=True)

    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy='subquery')

