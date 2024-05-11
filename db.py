from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# El engine permite a SQLAlquemy comunicarse con la base de datos en un dialecto concreto
#https://docs.sqlalchemy.org/en/14/core/engines.html
# al hacer intro en el objeto engine me da error y me suguiere descargar from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/tareas.db',
                       connect_args={"check_same_thread": False})
# ADVERTENCIA : Crear el engine no conecta inmediatemente con la DB, eso lo hacemos luego

# Ahora creamos la sesión, lo que nos permite realizar transaciones(operaciones dentro de la base de datos

# A continuacion nos dará error de nuevo y nos va sugerir que importemos sessionmaker
# Session va con mayusculas ya que es una Clase escrita de manera diferente

Session = sessionmaker(bind=engine)
session = Session()

# Aqui tambien nos dara error para que hagamos la descarga pero de entre las 2 opciones
#tenemos que escoger la de ORM tal y como arriba

# Ahora vamos al fichero models.py en los modelos (clases) donce queremos que se transformen
# Le añadiremos esta variavle y esto se encargara de mapear y vincular cada clase a cada tabla.

Base = declarative_base()


