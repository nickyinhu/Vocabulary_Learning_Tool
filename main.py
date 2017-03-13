import errno
import os
import sys
import MySQLdb

import choices


def start():
    category_choice = choices.get_category()
    scenario_choice = choices.get_scenario(category_choice)

if __name__ == "__main__":
    start()