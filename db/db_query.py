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