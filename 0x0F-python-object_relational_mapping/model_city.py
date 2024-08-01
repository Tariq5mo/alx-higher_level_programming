#!/usr/bin/python3
"""
A python file that contains the class definition of a City
and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKeyConstraint
from model_state import Base


class City(Base):
    """City class for database.

    Args:
        Base (Parent class)
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint('id'), ForeignKeyConstraint(['state_id'], ['states.id']))
