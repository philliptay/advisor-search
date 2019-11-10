from sys import argv
from database import Database
from professor import Professor
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)
#-------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if request.form.getlist('area') is not None:
            areas = request.form.getlist('area')

        database = Database()
        database.connect()
        results = database.search(areas)
        database.disconnect()


        print(results)

    html = render_template('index.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
