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
        keywords = input[1]
        keyResults = []
        areaResults = []

        cursor = self._connection.cursor()

        for keyword in keywords:
            if (keyword is not None) and (keyword.strip() != ''):

                # direct name hit
                stmtStr5 = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND name LIKE %s ORDER BY name'
                prep5 = '%'+keyword.lower().capitalize()+'%'
                cursor.execute(stmtStr5, (prep5,))
                rows5 = cursor.fetchall()
                if len(rows5) > 0:
                    for row5 in rows5:
                        keyResults.append(row5)

                # if no direct name hit, is it part of name, bio, title?
                else:
                    stmtStr2 = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND name LIKE %s ORDER BY name'
                    prep2 = keyword.lower().capitalize()+'%'
                    cursor.execute(stmtStr2, (prep2,))
                    rows2 = cursor.fetchall()
                    for row2 in rows2:
                        keyResults.append(row2)

                    stmtStr3 = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND bio LIKE %s ORDER BY name'
                    prep3 = keyword.lower()+'%'
                    cursor.execute(stmtStr3, (prep3,))
                    rows3 = cursor.fetchall()
                    for row3 in rows3:
                        keyResults.append(row3)

                    stmtStr4 = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs, past_theses WHERE areas.prof_id = profs.prof_id AND profs.prof_id = past_theses.prof_id AND title LIKE %s ORDER BY name'
                    prep4 = keyword.lower()+'%'
                    cursor.execute(stmtStr4, (prep4,))
                    rows4 = cursor.fetchall()
                    for row4 in rows4:
                        keyResults.append(row4)

        # search through inputted areas
        areas = areas[0].split(',')
        
        for area in areas:
            if (area is not None) and (area.strip() != ''):
                stmtStr = 'SELECT profs.name, areas.area, profs.prof_id FROM areas, profs WHERE areas.prof_id = profs.prof_id AND area LIKE %s ORDER BY name'
                prep = '%'+area.lower()+'%'
                cursor.execute(stmtStr, (prep,))
                rows = cursor.fetchall()
                for row in rows:
                    areaResults.append(row)


        cursor.close()

        results = [keyResults, areaResults]


        return results


    def profSearch(self, profid):

        cursor = self._connection.cursor()
        stmtStr = 'SELECT profs.name, profs.email, profs.bio, profs.pic_links FROM profs WHERE profs.prof_id = %s'
        cursor.execute(stmtStr, (profid,))
        rows = cursor.fetchall()
        for row in rows:
            name = row[0]
            contact = row[1]
            bio = row[2]
            picLink = row[3]

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

        professor = Professor(name, bio, areas, projects, titles, links, contact, picLink)
        return professor

    def rankResults(self, results):
        keyProfDict = {}
        areaProfDict = {}
        # loop through results list
        for prof in results[0]:
            name = prof[0]
            area = prof[1]
            profid = prof[2]
            # check if key is in dictionary
            if name in keyProfDict:
                keyProfDict[name].append(area)
            # if not then create new pair and set value to 0
            else:
                keyProfDict[name] = [profid, area]

        for prof in results[1]:
            name = prof[0]
            area = prof[1]
            profid = prof[2]
            # check if key is in dictionary
            if name in areaProfDict:
                areaProfDict[name].append(area)
            # if not then create new pair and set value to 0
            else:
                areaProfDict[name] = [profid, area]


        # sort the dictionary based on values
        keyProfDict = self.sort_by_values_len(keyProfDict)
        areaProfDict = self.sort_by_values_len(areaProfDict)
        profResults = []

        #make results the AND of area search and keyword search (absolutely disgusting code here)
        if len(keyProfDict) > 0 and len(areaProfDict) > 0:
            for aProf in areaProfDict:
                for kProf in keyProfDict:
                    for aKey in aProf.keys():
                        for kKey in kProf.keys():
                            if aKey == kKey:
                                profResults.append(aProf)
            return(profResults)

        if len(keyProfDict) > 0:
            return(keyProfDict)

        else:
            return(areaProfDict)


    #taken from stack overflow
    def sort_by_values_len(self, dict):
        dict_len= {key: len(value) for key, value in dict.items()}
        import operator
        sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
        sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
        return(sorted_dict)

    def favoritedProfSearch(self, username):
        cursor = self._connection.cursor()
        stmtStr =  'SELECT profs.name, areas.area, favorited_profs.prof_id FROM areas, profs, favorited_profs WHERE favorited_profs.prof_id = profs.prof_id AND areas.prof_id = favorited_profs.prof_id AND username = %s ORDER BY name'
        cursor.execute(stmtStr, (username,))
        rows = cursor.fetchall()
        return [rows, []]

    def isProfFavorited(self, username, prof_id):
        cursor = self._connection.cursor()
        stmtStr =  'SELECT username, prof_id FROM favorited_profs WHERE username = %s AND prof_id = %s'
        cursor.execute(stmtStr, (username, prof_id))
        row = cursor.fetchone()
        if row is None:
            return False
        return True

    # check user in database - if not, add
    def insertUser(self, username):
        cursor = self._connection.cursor()
        stmtStr = 'SELECT username FROM users WHERE username = %s'
        cursor.execute(stmtStr, [username])

        row = cursor.fetchone()
        if row is None:
            stmt = "INSERT INTO users (username) VALUES (%s)"
            cursor.execute(stmt, (username,))
            self._connection.commit()
        cursor.close()

    def updateFavoritedProf(self, username, prof_id):
        if prof_id == 'None':
            return
        cursor = self._connection.cursor()
        if not self.isProfFavorited(username, prof_id):
            stmt = 'INSERT INTO favorited_profs (username, prof_id) VALUES (%s, %s)'
            cursor.execute(stmt, (username, prof_id))
            self._connection.commit()
        else :
            stmt = 'DELETE FROM favorited_profs WHERE username = %s AND prof_id = %s'
            cursor.execute(stmt, (username, prof_id))
            self._connection.commit()
        cursor.close()
