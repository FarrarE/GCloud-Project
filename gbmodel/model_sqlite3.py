from .Model import Model
from datetime import date
import sqlite3

DB_FILE = 'entries.db'

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try: 
            cursor.execute("Select count(rowid) from recipebook")
        except sqlite3.OperationalError:
            cursor.execute("create table recipebook (title text, author text, signed_on date, recipe)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: title, author, date, recipe
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipebook")
        return cursor.fetchall()

    def insert(self, title, author, recipe):
        """
        Inserts entry into database
        :param title: String
        :param author: String
        :param date: date
        :param recipe: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'title':title, 'author':author, 'date':date.today(), 'recipe':recipe}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipebook (title, author, signed_on, recipe) VALUES (:title, :author, :date, :recipe)", params)
        connection.commit()
        cursor.close()
        return True
