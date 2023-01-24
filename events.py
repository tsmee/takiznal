from db_model import Events
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Event:
    def __init__(self, is_active, created, finished, description):
        self.is_active = is_active
        self.created = created
        self.finished = finished
        self.description = description
        self.id = None
        engine = create_engine('sqlite:///example.db', echo=True)

        # Create a session
        session = Session(bind=engine)
        session.execute('PRAGMA foreign_keys = ON;')
        new_event = Events(active=self.is_active, created=self.created, finished=self.finished,
                           description=self.description)
        session.add(new_event)
        session.commit()
        self.id = new_event.id


aaa = Event(1, 999, 999, "aaa")
print(aaa.id)
print(aaa.description)