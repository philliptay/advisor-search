import os
import psycopg2
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/advisordb'
db = SQLAlchemy(app)


def main():
    filename = 'Cos Department Data'
    conn = psycopg2.connect(database='advisordb', host='127.0.0.1', port='5432')
    wb = pd.read_excel(filename+'.xlsx')

    #    for sheet in wb:
#        wb[sheet].to_sql(sheet,con, index=False)
    con.commit()
    con.close()

if __name__ == '__main__':
    main()
