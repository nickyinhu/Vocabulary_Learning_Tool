from peewee import *
from playhouse.db_url import connect

# database = MySQLDatabase('sql9170918', **{'host': 'sql9.freesqldatabase.com', 'password': 'ZGDMCzDtkP', 'user': 'sql9170918'})

database = connect('mysql://sql9170918:ZGDMCzDtkP@sql9.freesqldatabase.com:3306/sql9170918')

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

class Words(BaseModel):
    meaning = TextField()
    scenario = ForeignKeyField(db_column='scenario_id', rel_model=Scenarios, to_field='id')
    word = CharField()

    class Meta:
        db_table = 'words'

class SampleSentence(BaseModel):
    sentence = TextField()
    word = ForeignKeyField(db_column='word_id', null=True, rel_model=Words, to_field='id')

    class Meta:
        db_table = 'sample_sentence'

class User(BaseModel):
    email = TextField()
    pw_hash = TextField()
    user = PrimaryKeyField(db_column='user_id')
    username = TextField()

    class Meta:
        db_table = 'user'

