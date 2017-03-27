import errno
import os
import sys
from db.db_query import *


def get_category():
    category_list = get_all_categories()

    for category in category_list:
        print "{}: {}".format(category.id, category.name)

    choice = None
    category = None
    while category is None:

        choice = raw_input("\nChoose the category")
        try:
            choice = int(choice)
        except ValueError:
            print 'sorry,', choice, 'is not a valid choice'
            continue

        try:
            category = get_category_by_id(choice)
        except IndexError:
            print 'sorry,', choice, 'is not a valid choice'

    print "Your category choice: {}\n".format(category.name)
    return choice


def get_scenario(category_id):
    scenarios_list = get_scenario_by_category(category_id)
    count = 1
    for scenario in scenarios_list:
        print "{}: {}".format(count, scenario.event)
        count += 1

    choice = None
    scenario = None
    while scenario is None:

        choice = raw_input("\nChoose event to learn words")
        try:
            choice = int(choice)
        except ValueError:
            print 'sorry,', choice, 'is not a valid choice'
            continue

        try:
            scenario = scenarios_list[choice - 1]
        except IndexError:
            print 'sorry,', choice, 'is not a valid choice'

    print "Your event choice: {}\n".format(scenario.event)
    return scenario.id


def get_words(scenario_id):
    word_list = get_words_by_scenario(scenario_id)

    count = 1
    for word in word_list:
        print "{} {}: {}".format(count, word.word, word.meaning)
        count += 1

    choice = None
    word_choice = None
    while word_choice is None:

        choice = raw_input("\nChoose word to see sample sentence")
        try:
            choice = int(choice)
        except ValueError:
            print 'sorry,', choice, 'is not a valid choice'
            continue

        try:
            word_choice = word_list[choice - 1]
        except IndexError:
            print 'sorry,', choice, 'is not a valid choice'

    print "Your word choice: {}\n".format(word_choice.word)
    return word_choice.id

def get_sentence(sentence_id,category_id,scenario_id):
    sentences = get_sentence_by_id(sentence_id)
    count = 1
    for sentence in sentences:
        print "Sample {}: {}".format(count, sentence.sentence)
        count+=1

    options = {
        1: "Choose another category",
        2: "Choose another scenario of the current category",
        3: "Choose another word to see sample sentence",
        4: "Exit",
    }


    choice = None
    option_choice = None
    print "\n\n"
    for k in options.keys():
        print "{}, {}".format(k, options[k])
    while choice is None:
        choice = raw_input("\nPlease choose from the options")
        try:
            choice = int(choice)
        except ValueError:
            print 'sorry,', choice, 'is not a valid choice'
            continue
        if choice not in options.keys():
            print 'sorry,', choice, 'is not a valid choice'
        else:
            option_choice = choice

    print "Your option choice: {}\n".format(options[option_choice])
    return option_choice