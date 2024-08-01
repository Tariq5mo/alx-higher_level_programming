#!/usr/bin/python3
"""
A python file that contains the class definition of a State
and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class for database.

    Args:
        Base (Parent class)
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    __table_args__ = (UniqueConstraint('id'), )
