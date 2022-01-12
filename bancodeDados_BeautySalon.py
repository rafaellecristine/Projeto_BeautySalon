from peewee import *

db = SqliteDatabase('database.sqlite')
class BaseModel(Model):
    class Meta:
        database = db

class Clientes(BaseModel):
    Nome = TextField(null=False)
    Telefone = TextField(null=False)
    Serviço = TextField(null=False)
    Horário = TextField(null=False)

idCliente = ForeignKeyField(Clientes, backref='Clientes')

#Clientes.create_table()

