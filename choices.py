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

        choice = raw_input("\nPlease choose which category of events you want to learn words")
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

    for scenario in scenarios_list:
        print "{}: {}".format(scenario.id, scenario.event)

    choice = None
    scenario = None
    while scenario is None:

        choice = raw_input("\nPlease choose which event you want to learn words")
        try:
            choice = int(choice) - 1
        except ValueError:
            print 'sorry,', choice, 'is not a valid choice'
            continue

        try:
            scenario = scenarios_list[choice]
        except IndexError:
            print 'sorry,', choice, 'is not a valid choice'

    print "Your event choice: {}\n".format(scenario.event)
    return choice
