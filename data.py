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
