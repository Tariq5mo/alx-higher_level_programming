#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == '__main__':
    num_args = len(argv)
    if num_args == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        ss = sessionmaker(bind=engine)
        session = ss()
        try:
            li = session.query(State).order_by(State.id).first()
            print("{}: {}".format(li.id, li.name))
        except Exception:
            print("Nothing")
