from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_model import Events, Options, Results

# Connect to the database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a session
session = Session(bind=engine)
session.execute('PRAGMA foreign_keys = ON;')

# new_event = Events(active=1, created=20, description="blah")
# session.add(new_event)

new_option = Options(event_id=1, description="Модная опция")
session.add(new_option)
session.commit()

