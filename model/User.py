
from sqlalchemy import Table, Column, ForeignKey, INT, VARCHAR, DATE, TEXT, BOOLEAN, BIGINT, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(INT, primary_key=True, autoincrement=True)
    login = Column(VARCHAR)
    money_amount = Column(INT)
    card_number = Column(VARCHAR)
    status = Column(BOOLEAN)

    password = relationship("UserPassword")


class UserPassword(Base):
    __tablename__ = "user_passwords"

    user_id = Column(INT, ForeignKey('users.id'), primary_key=True)
    password = Column(VARCHAR)

    user = relationship("User")
