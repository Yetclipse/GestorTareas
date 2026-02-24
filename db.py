from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
#Crea la carpeta de database si no existe ya que engine no la crea
os.makedirs('database', exist_ok=True)
engine = create_engine('sqlite:///database/tareas.db',
connect_args={'check_same_thread': False})

sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()
Base = declarative_base()