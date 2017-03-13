from peewee import *

database = MySQLDatabase('6460', **{'host': 'localhost', 'password': 'password', 'user': '6460'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Category(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'category'

class Scenarios(BaseModel):
    category = ForeignKeyField(db_column='category_id', rel_model=Category, to_field='id')
    event = CharField()

    class Meta:
        db_table = 'scenarios'
