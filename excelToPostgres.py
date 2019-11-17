import os
import psycopg2
import pandas as pd
from flask import Flask


def main():
    filename = 'Cos Department Data'
    conn = psycopg2.connect(database='advisordb', user='admin', password='thesissearchboyz420', host='localhost', port='5432')
    cursor = conn.cursor()
    wb = pd.read_excel(filename+'.xlsx')
    for i, row in wb.iterrows():

        profsStmt = 'INSERT INTO profs (prof_id, name, bio, email) VALUES (%s,%s,%s,%s)'
        cursor.execute(profsStmt, (i, row['name'], row['bio'], row['email']+'@cs.princeton.edu'))

        if not pd.isna(row['areas']):
            areasList = row['areas'].replace(';', ',').split(', ')
            for area in areasList:
                areaStmt = 'INSERT INTO areas (area, prof_id) VALUES (%s,%s)'
                cursor.execute(areaStmt, (area.strip().lower(), i))

        if not pd.isna(row['Research Projects']):
            projsList = row['Research Projects'].replace(';', ',').split(', ')
            for proj in projsList:
                projStmt = 'INSERT INTO projects (title, prof_id) VALUES (%s,%s)'
                cursor.execute(projStmt, (proj.strip().lower(), i))

        if not pd.isna(row['Past Theses Advised (Titles)']):
            titlesList = row['Past Theses Advised (Titles)'].split(';')
            linksList = row['Past Theses Advised (Links)'].split(';')
            for j in range(len(titlesList)):
                thesisStmt = 'INSERT INTO past_theses (title, link, prof_id) VALUES (%s,%s,%s)'
                cursor.execute(thesisStmt, (titlesList[j].strip(), linksList[j].strip(), i))




    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
