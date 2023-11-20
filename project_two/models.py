from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from main import engine

Base = declarative_base()


from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    ingredients = Column(
        Text,
        nullable=False,
    )

    instructions = Column(
        Text,
        nullable=False,
    )

    chef_id = Column(
        Integer,
        ForeignKey('chefs.id')
    )

    chef = relationship("Chef", back_populates="recipes")


class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    recipes = relationship("Recipe", back_populates="chef")


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
#
# class Order(Base):
#     __tablename__ = 'orders'
#
#     id = Column(Integer, primary_key=True)
#     is_completed = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship('User')


# Base.metadata.create_all(engine)
