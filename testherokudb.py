import os
import psycopg2
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/advisordb'
db = SQLAlchemy(app)
heroku = Heroku(app)


def main():
  db.create_all()

if __name__ == '__main__':
    main()
