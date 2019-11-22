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

    def search(self, input):

        areas = input[0]
        keyword = input[1].toLower()
        if (keyword is None) or (keyword.strip() == ''):
            keyword = ''
        else:
            keyword = keyword.strip().lower()

        results = []

        if (areas is not None):
            cursor1 = self._connection.cursor()
            for area in areas:
                stmtStr = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND area LIKE %s ORDER BY name'
                prep = '%'+area.lower()+'%'
                cursor1.execute(stmtStr, (prep,))
                rows = cursor1.fetchall()
                for row in rows:
                    results.append(row)


        if (keyword != ''):
            cursor2 = self._connection.cursor()
            stmtStr = 'SELECT profs.name, profs.bio, past_theses.title, areas.area, prof.prof_id FROM profs, past_theses, area WHERE profs.prof_id = past_theses.prof_id'
            cursor2.execute(stmStr)
            rows2 = cursor2.fetchall()
            for row2 in rows2:
                arg1 = list(str(row2[0]).lower())
                arg2 = list(str(row2[1]).lower())
                arg3 = list(str(row2[2]).lower())
                arg4 = list(keyword)
                inc1 = 0
                inc2 = 0

                # Search for keyword in professor names
                while (inc1 < len(arg1)):
                    if (arg1[inc1] == arg4[inc2]) and (inc2 < len(arg4) - 1):
                        inc2 += 1
                    elif (arg1[inc1] == arg4[inc2]) and (inc2 >= len(arg4) - 1):
                        newRow = [row2[0], row2[3], row2[4]]
                        results.append(newRow)
                        break
                    else:
                        inc2 = 0
                    inc1 += 1

                inc1 = 0
                inc2 = 0

                # Search for keyword in professor bios
                while (inc1 < len(arg2)):
                    if (arg2[inc1] == arg4[inc2]) and (inc2 < len(arg4) - 1):
                        inc2 += 1
                    elif (arg2[inc1] == arg4[inc2]) and (inc2 >= len(arg4) - 1):
                        newRow = [row2[0], row2[3], row2[4]]
                        results.append(newRow)
                        break
                    else:
                        inc2 = 0
                    inc1 += 1

                inc1 = 0
                inc2 = 0

                #search for keyword in past_theses titles
                while (inc1 < len(arg3)):
                    if (arg3[inc1] == arg4[inc2]) and (inc2 < len(arg4) - 1):
                        inc2 += 1
                    elif (arg3[inc1] == arg4[inc2]) and (inc2 >= len(arg4) - 1):
                        newRow = [row2[0], row2[3], row2[4]]
                        results.append(newRow)
                        break
                    else:
                        inc2 = 0
                    inc1 += 1

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

        if len(titles) == 0:
            titles = 'This advisor has no previous works advised.'
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

    def rankResults(results):
        profDict = {}
        # loop through results list
        for prof in results:
            name = prof[0]
            area = prof[1]
            profid = prof[2]
            # check if key is in dictionary
            if name in profDict:
                profDict[name].append(area)
            # if not then create new pair and set value to 0
            else:
                profDict[name] = [profid, area]
        # sort the dictionary based on values
        profDict = self.sort_by_values_len(profDict)
        # return dictionary
        return(profDict)


    #taken from stack overflow
    def sort_by_values_len(dict):
        dict_len= {key: len(value) for key, value in dict.items()}
        import operator
        sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
        sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
        return(sorted_dict)
