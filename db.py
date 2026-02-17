from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database/tareas.db',
connect_args={'check_same_thread': False})

sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()
Base = declarative_base()