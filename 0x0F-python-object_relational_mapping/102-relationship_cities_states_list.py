#!/usr/bin/python3
"""
Model: 100-relationship_states_cities.py
Author: Sheriff Abdulfatai
"""


if __name__ == "__main__":
    from sys import argv as a
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id).all()

    for city in query:
        print(f'{city.id}: {city.name} -> {city.state.name}')
