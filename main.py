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

    allAreas = ['Computational Biology', 'Computer Architecture', 'Economics/Computation', 'Graphics', 'Vision', 'Machine Learning', 'AI', 'Natural Language Processing', 'Policy', 'Programming Languages/Compilers', 'Security & Privacy', 'Systems', 'Theory']
    database = Database()
    database.connect()
    results = database.search(allAreas)
    database.disconnect()

    profData = Professor('', '', '', '', '')
    if request.method == 'POST':
        if request.form.getlist('area') is not None:
            areas = request.form.getlist('area')

        database = Database()
        database.connect()
        results = database.search(areas)
        database.disconnect()

    if request.method == 'GET':
        if request.args.get('profid') is not None:
            profid = request.args.get('profid')

            database = Database()
            database.connect()
            profData = database.profSearch(profid)
            database.disconnect()

    html = render_template('index.html', professors = results, prof = profData)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
