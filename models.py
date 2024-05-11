from db import Base
from sqlalchemy import Column, Integer, Boolean, String

import db
# para poder utilizar una clase para hacer una tabla de la db tenemos que importar la db
# e indicar a la clase la ruta y Base (con mayuscula ya que es una clase)

class Tarea(db.Base):

    __tablename__ = "tarea"
    __table_args__ ={'sqlite_autoincrement': True} # esto autoincrementa la primatykey de la tabla
#mirar en documentacion para ver como se define el primaty key y
# como se hace para que un valor no este vacio el caso de id_persona
    id =Column(Integer, primary_key =True)  # habra cosas que estan subrayadas y es que que que autoimportar
    contenido = Column(String (200), nullable=False)   #OJO TIENE QUE IMPORTAR EL MISMO SITIO
    hecha = Column(Boolean)

#nombre y edad tiene que tener el mismo nombre que abajo

#__tablename__ se pone el nombre de la tabla en minisculas y singular
#__table_args__ ashi se pone las configuraciones de la tabla

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha
        print('Tarea creada con exito')

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

