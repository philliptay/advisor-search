from sys import argv
from database import Database
from professor import Professor
from re import sub
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from CASClient import CASClient

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# generated by os.urandom(16)
app.secret_key = b'm\xb5\xe6\xef4\xb5\x02_\x8f\xe4\xffpw\xccu\xc4'
heroku = Heroku(app)
db = SQLAlchemy(app)

#-------------------------------------------------------------------------------
@app.route('/login', methods=['GET'])
def login():
    CASClient().authenticate()
    return redirect(url_for('index'))

#-------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
         session['profs'] = None
         html = render_template('login.html')
         response = make_response(html)
         return(response)

    username = session['username']

    allAreas = ['Computational Biology', 'Computer Architecture', 'Economics/Computation', 'Graphics', 'Vision', 'Machine Learning', 'AI', 'Natural Language Processing', 'Policy', 'Programming Languages/Compilers', 'Security & Privacy', 'Systems', 'Theory']
    profList = session['profs']
    profData = Professor('', '', '', '', '', '', '')

    if profList is None:
        profList = []

    if request.method == 'POST':
        #go through array returned by select2 searchbar and check if each item is area or keyword
        #build an area array and keyword array

        areas = []
        keywords = []
        inputs = request.args.getlist('data')
        for input in inputs:
            if input in allAreas:
                areas.append(input)
            else:
                keywords.append(input)
        if len(areas) == 0 and len(keywords) == 0:
            areas = allAreas


        #just for demoing keyword search
        keywords = request.args.get('search')
        areas = []

        searchInput = [areas, keywords]

        database = Database()
        database.connect()
        results = database.search(searchInput)
        profDict = database.rankResults(results)

        profList = []
        for prof in profDict:
            for key in prof:
                profname = key
                areas = prof[profname][1:]
                profid = prof[profname][0]
            info = [profname, areas, profid] #create a list for the prof
            profList.append(info)
        database.disconnect()

        profTitles = ''
        profLinks = ''

    if request.method == 'GET':
        if request.args.get('profid') is not None:
            profid = request.args.get('profid')
            if  profid.strip() == '':
                errorMsg = 'Missing profid'
                return redirect(url_for('error', errorMsg=errorMsg))
            try:
                int(profid)
            except ValueError:
                errorMsg = 'Profid is not numeric'
                return redirect(url_for('error', errorMsg=errorMsg))

            database = Database()
            database.connect()
            profData = database.profSearch(profid)
            database.disconnect()

            profTitles = profData.getTitles()
            profLinks = profData.getLinks()

        else:
            profTitles = ''
            profLinks = ''

    html = render_template('index.html', user=username, professors = profList, prof = profData, titles = profTitles, links = profLinks)
    response = make_response(html)
    # profStr = ''
    # for prof in profList:
    #     profStr += prof + ','
    # areasStr.rstrip(',')
    session['profs'] = profList
    return(response)

#-------------------------------------------------------------------------------
@app.route('/resources')
def resources():
    if 'username' not in session:
         return redirect(url_for('index'))
    html = render_template('resources.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------
@app.route('/error')
def error():
    if 'username' not in session:
        return redirect(url_for('index'))
    errorMsg = request.args.get('errorMsg')

    html = render_template('error.html', errorMsg=errorMsg)
    response = make_response(html)
    return(response)
#-------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    return CASClient().logout()
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
