import os
import psycopg2
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

DATABASE_URL = 'postgres://mzehsxrhlmmrdp:7229a3ce7cdddcfd25d960016bab27a25ecd1163a471263f73d2c64d78f15d70@ec2-174-129-252-252.compute-1.amazonaws.com:5432/d56v6b7trhtuts'

def main():
 conn = psycopg2.connect(DATABASE_URL, sslmode='require')
 stmt = 'SELECT * FROM areas'
 cursor = conn.cursor()
 cursor.execute(stmt)
 row = cursor.fetchone()
 while row is not None:
     print(row[0])
     row = cursor.fetchone()

if __name__ == '__main__':
    main()
