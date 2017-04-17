from db.models import *


def get_scenario_by_category(category_id):
    scenarios = Scenarios.select().where(Scenarios.category == category_id)
    if scenarios is not None:
        return scenarios


def get_all_categories():
    categories = Category.select()
    if categories is not None:
        return categories

def get_words_by_scenario_name(scenario_name):
    words = Words.select(Words).join(Scenarios).where(Scenarios.name == scenario_name)
    if words is not None:
        return words

def get_sentence_by_word(word):
    sentences = SampleSentence.select(SampleSentence).join(Words).where(Words.word == word)
    if sentences is not None:
        return sentences

def get_scenario_by_category_name(category_name):
    scenarios = Scenarios.select(Scenarios).join(Category).where(Category.name == category_name)
    if scenarios is not None:
        return scenarios
