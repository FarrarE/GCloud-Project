"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipes = dict()

    def select(self):
        """
        Returns recipes list of lists
        Each list in recipes contains: title, author, date, recipe
        :return: List of lists
        """
        return self.recipes

    def insert(self, title, author, recipe):
        """
        Appends a new list of values representing new recipe into recipes
        :param title: String
        :param author: String
        :param recipe: String
        :return: True
        """
        params = dict(author=author, date=date.today(), recipe=recipe)
        self.recipes[title] = params
        return True
