from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()


class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    active = Column(Integer)
    created = Column(Integer)
    finished = Column(Integer)
    description = Column(String)


class Options(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    description = Column(String)


class Results(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    option_id = Column(Integer, ForeignKey('options.id'))


