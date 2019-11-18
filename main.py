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
    areas = request.form.getlist('area')
    if request.form.getlist('area') is not None:
        areas = allAreas

    database = Database()
    database.connect()
    results = database.search(areas)
    database.disconnect()

    profData = Professor('', '', '', '', '')
    if request.method == 'POST':
        if request.form.getlist('area') is not None:
            areas = request.form.getlist('area')

        database = Database()
        database.connect()
        searchResults = database.search(areas)
        profDict = rankResults(searchResults) #rank the results
        profList = []
        # turn results into list of lists to be displayed
        for prof in profDict:
            for key in prof:
                profname = key
                areas = prof[profname][1:]
                profid = prof[profname][0]
            info = [profname, areas, profid] #create a list for the prof
            profList.append(info)

        database.disconnect()

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

    html = render_template('index.html', professors = profList, prof = profData)
    response = make_response(html)
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
