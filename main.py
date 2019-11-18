from sys import argv
from database import Database
from professor import Professor
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'big secret boy'
heroku = Heroku(app)
db = SQLAlchemy(app)
#-------------------------------------------------------------------------------
@app.route('/')
def login():
    session['profs'] = None
    html = render_template('login.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/home', methods=['GET', 'POST'])
def index():

    allAreas = ['Computational Biology', 'Computer Architecture', 'Economics/Computation', 'Graphics', 'Vision', 'Machine Learning', 'AI', 'Natural Language Processing', 'Policy', 'Programming Languages/Compilers', 'Security & Privacy', 'Systems', 'Theory']
    profList = session['profs']
    profData = Professor('', '', '', '', '', '', '')

    if profList is None:
        profList = []

    if request.method == 'POST':
        areas = request.form.getlist('area')
        if len(areas) == 0:
            areas = allAreas

        database = Database()
        database.connect()
        results = database.search(areas)
        profDict = rankResults(results)

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

    html = render_template('index.html', professors = profList, prof = profData, titles = profTitles, links = profLinks)
    response = make_response(html)
    # profStr = ''
    # for prof in profList:
    #     profStr += prof + ','
    # areasStr.rstrip(',')
    session['profs'] = profList
    return(response)
#-------------------------------------------------------------------------------
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
    profDict = sort_by_values_len(profDict)
    # return dictionary
    return(profDict)


#taken from stack overflow
def sort_by_values_len(dict):
    dict_len= {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
    return(sorted_dict)
#-------------------------------------------------------------------------------
@app.route('/resources')
def resources():
    html = render_template('resources.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------
@app.route('/error')
def error():

    errorMsg = request.args.get('errorMsg')

    html = render_template('error.html', errorMsg=errorMsg)
    response = make_response(html)
    return(response)
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
