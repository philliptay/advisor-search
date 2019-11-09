from sqlite3 import connect
from sys import stderr, exit
from os import path
from professor import Professor

class Database:

    def __init__(self):
        self._connection = None

    def connect(self):
        DATABASE_NAME = 'reg.sqlite'
        if not path.isfile(DATABASE_NAME):
            raise Exception('Database connection failed')
        self._connection = connect(DATABASE_NAME)

    def disconnect(self):
        self._connection.close()

    # def search(self, inputs):
