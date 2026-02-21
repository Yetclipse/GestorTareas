import db
from sqlalchemy import Column, Date, Integer, String, Boolean
''' 
Creamos una clase llamada Tarea  
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá  
luego para la base de datos)  
Esta clase va a almacenar toda la información referente a una tarea  
'''
class Tarea(db.Base):
    __tablename__ = 'tarea'
    id = Column(Integer, primary_key=True) # Identificador unico de cada tarea
    contenido = Column(String(200), nullable=False) # Contenido de la tarea, Max 200 Caracteres
    hecho = Column(Boolean)
    categoria = Column(String(50), nullable=True) # Categoria de la tarea, Max 50 Caracteres, Puede ser nula
    fecha_limite = Column(Date, nullable=True) #"YYYY-MM-DD", Puede ser nula
    def __init__(self, contenido, hecho, categoria=None, fecha_limite=None):
        self.contenido = contenido
        self.hecho = hecho
        self.categoria = categoria
        self.fecha_limite = fecha_limite

    def __repr__(self):
        return 'Tarea {} {} ({})'.format(self.id, self.contenido, self.hecho)

    def __str__(self):
        return 'Tarea {} {} ({})'.format(self.id, self.contenido, self.hecho)

