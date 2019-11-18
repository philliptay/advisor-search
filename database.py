from sqlite3 import connect
import psycopg2
from pandas import isna
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

    def search(self, areas):

        results = []

        cursor = self._connection.cursor()
        for area in areas:
            stmtStr = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND area LIKE %s ORDER BY name'
            prep = '%'+area.lower()+'%'
            cursor.execute(stmtStr, (prep,))
            rows = cursor.fetchall()
            for row in rows:
                results.append(row)

        return results

    def profSearch(self, profid):

        cursor = self._connection.cursor()
        stmtStr = 'SELECT profs.name, profs.email, profs.bio FROM profs WHERE profs.prof_id = %s'
        cursor.execute(stmtStr, (profid,))
        rows = cursor.fetchall()
        for row in rows:
            name = row[0]
            contact = row[1]
            bio = row[2]

        areas = []
        projects = []
        titles = []
        links = []


        stmtStr = 'SELECT areas.area FROM areas WHERE areas.prof_id = %s'
        cursor.execute(stmtStr, (profid,))
        areas = cursor.fetchall()
        if len(areas) == 0:
            areas = 'No research areas found.'

        stmtStr = 'SELECT projects.title FROM projects WHERE projects.prof_id = %s'
        cursor.execute(stmtStr, (profid,))
        projects = cursor.fetchall()
        if len(projects) == 0:
            projects = 'No projects found.'

        stmtStr = 'SELECT past_theses.title, past_theses.link FROM past_theses WHERE past_theses.prof_id = %s'
        cursor.execute(stmtStr, (profid,))
        rows = cursor.fetchall()

        for row in rows:
            titles.append(row[0])
            links.append(row[1])

        if contact == 'NaN':
            contact = 'No contact provided.'

        if bio == 'NaN':
            bio = 'No bio provided.'

        if titles == 'NaN':
            titles = 'This advisor has no previous works advised.'

        if links == 'NaN':
            links = ''

        professor = Professor(name, bio, areas, projects, titles, links, contact)
        return professor

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
