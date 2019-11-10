from sqlite3 import connect
import psycopg2
from sys import stderr, exit
from os import path
from professor import Professor

class Database:

    def __init__(self):
        self._connection = None

    def connect(self):
        DATABASE_URL = 'postgres://mzehsxrhlmmrdp:7229a3ce7cdddcfd25d960016bab27a25ecd1163a471263f73d2c64d78f15d70@ec2-174-129-252-252.compute-1.amazonaws.com:5432/d56v6b7trhtuts'
        self._connection = psycopg2.connect(DATABASE_URL, sslmode='require')

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

    def loginSearch(self, username, password):
        #check that username is in Database
        #if not found, print error message: username does not exist
        #check that password matches username
        #if not print incorrect password
        cursor = connection.cursor()
        stmtStr = 'SELECT username, password FROM login WHERE username = ?'
        cursor.execute(stmtStr, [username])

        row = cursor.fetchone()
        if row is None:
            cursor.close()
            connection.close()
            return "username does not exist error"
        else:
            if password != row[1]:
                cursor.close()
                connection.close()
                return "incorrect password"
            else:
                cursor.close()
                connection.close()
                return "success"

    def addLogin(self, username, password):
        userpair = '(' + username + ', ' + password + ')'
        cursor = connection.cursor()
        stmtStr = 'SELECT username FROM login WHERE username = ?'
        cursor.execute(stmtStr, [username])
        row = cursor.fetchone()
        #check that username is not already there
        if row is not None:
            cursor.close()
            connection.close()
            # if so send message that user exists, pick a different name
            return "username already exists, please select a different username"
        else:
            cursor.close()
            connection.close()

            #add username to username column and password to password column
            cursor = connection.cursor()
            stmtStr2 = 'INSERT INTO login (username, password) VALUES ?'
            cursor.execute(stmtStr2, [userpair])
            connection.commit()
            cursor.close()
            connection.close()
            return 'successful creation of new user'
