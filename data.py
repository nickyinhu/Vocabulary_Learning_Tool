import errno
import os
import sys
from db.db_query import *


def get_category_list():
    category_list = get_all_categories()
    return category_list

def get_scenario_list(category_name):
    scenarios_list = get_scenario_by_category(category_name)
    return scenarios_list

def get_word_list(scenario_name):
    word_list = get_words_by_scenario(scenario_name)
    return word_list

def get_sentence_list(word):
    sentence_list = get_sentence_by_word(word)
    return sentence_list

def get_word(word_id):
    word = get_word_by_id(word_id)
    return word

def get_user_id(username):
    user = get_user_by_username(username)
    return user

def get_user(user_id):
    user = get_user_by_userid(user_id)
    return user

def get_user(user_id):
    user = check_password_hash(user_id)
    return user

def create_user(username,email,pw_hash):
    create_user_in_db(username,email,pw_hash)

