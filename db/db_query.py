from db.models import *


def get_scenario_by_category(categoryID):
    scenarios = Scenarios.select().where(Scenarios.category == categoryID)
    if scenarios is not None:
        return scenarios


def get_all_categories():
    categories = Category.select()
    if categories is not None:
        return categories


def get_category_by_id(id):
    categories = Category.select().where(Category.id == id)
    if categories is not None:
        return categories[0]

def get_words_by_scenario(id):
    words = Words.select().where(Words.scenario == id)
    if words is not None:
        return words

def get_sentence_by_id(id):
    sentences = SampleSentence.select().where(SampleSentence.word == id)
    if sentences is not None:
        return sentences
