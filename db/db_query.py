from db.models import *
from pprint import pprint

def get_all_categories():
    categories = Category.select()
    if categories.exists():
        return categories

def get_words_by_scenario(scenario_name):
    words = Words.select(Words).join(Scenarios).where(Scenarios.event == scenario_name)
    if words.exists():
        return words

def get_word_by_id(word_id):
    try:
        word = Words.get(Words.id == word_id)
    except Words.DoesNotExist:
        word = None
    return word

def get_sentence_by_word(word):
    sentences = SampleSentence.select(SampleSentence).join(Words).where(Words.word == word)
    if sentences.exists():
        return sentences

def get_scenario_by_category(category_name):
    scenarios = Scenarios.select(Scenarios).join(Category).where(Category.name == category_name)
    if scenarios.exists():
        return scenarios

def get_user_by_username(username):
    try:
        user = User.get(User.username == username)
    except User.DoesNotExist:
        user = None
    return user

def get_user_by_userid(user_id):
    try:
        user = User.get(User.user == user_id)
    except User.DoesNotExist:
        user = None
    return user

def create_user_in_db(username,email,pw_hash):
    User.insert(username = username, email = email, pw_hash = pw_hash).execute()