from sqlite3 import connect
from sys import stderr, exit
from os import path
from professor import Professor

class Database:

    def __init__(self):
        self._connection = None

    def connect(self):
        DATABASE_NAME = 'advisordb.postgres'
        if not path.isfile(DATABASE_NAME):
            raise Exception('Database connection failed')
        self._connection = connect(DATABASE_NAME)

    def disconnect(self):
        self._connection.close()

    # def search(self, inputs):
        # cursor = connection.cursor()
        # cursor.execute('SELECT profs.name, profs.contact, areas.area, profs.bio FROM areas, profs WHERE areas.profid = profs.profid AND area = \"' + area + '\"')
        # rows = cursor.fetchall()
        # for row in rows:
        # add prof name to table in html code
        # pass cookies for each profs contact and bio
        # not sure how it will work for profs with multiple areas
