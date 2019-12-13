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
    # CASClient().authenticate()
    # return redirect(url_for('index'))
    html = render_template('login.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():

    # if 'username' not in session:
    #      session['profs'] = None
    #      html = render_template('login.html')
    #      response = make_response(html)
    #      return(response)

    username = session['username']

    html = render_template('index.html', user=username)
    response = make_response(html)


    return(response)

#-------------------------------------------------------------------------------

@app.route('/searchresults')
def searchResults():
    allAreas = ['Computational Biology', 'Computer Architecture', 'Economics/Computation', 'Graphics', 'Vision', 'Machine Learning', 'AI', 'Natural Language Processing', 'Policy', 'Programming Languages/Compilers', 'Security & Privacy', 'Systems', 'Theory']

    areas = request.args.getlist('areas')
    keywords = request.args.getlist('keywords')

    # areas = []
    # keywords = []
    # tags = request.args.getlist('tags')
    # for tag in tags:
    #     if tag in allAreas:
    #         areas.append(tag)
    #     else:
    #         keywords.append(tag)

    searchInput = [areas, keywords]
    print(searchInput)

    database = Database()
    database.connect()
    results = database.search(searchInput)
    profDict = database.rankResults(results)
    database.disconnect()

    profList = []
    for prof in profDict:
        for key in prof:
            profname = key
            areas = prof[profname][1:]
            profid = prof[profname][0]
            info = [profname, areas, profid] #create a list for the prof
            profList.append(info)

    resultsnum = len(profList)

    html = '<h3>'+str(resultsnum)+' Search Results</h3><h3>Advisors</h3><div id="resultsWrapper"><ul class="marginless">'
    for prof in profList:
        topAreas = ''
        for i in range(min(3, len(prof[1]))) :
            topAreas += prof[1][i]+', '
        topAreas = topAreas.rstrip(', ')
        html += '<a href="#" onclick="getProfResults('+str(prof[2])+');"><li class="list-group-item" tabindex="0"><strong>'+str(prof[0])+'</strong><br><span>Top Areas: '+ topAreas +'</span></li></a>'
    html += '</ul></div>'
    html.encode('utf-8')
    response = make_response(html)

    return(response)

#-------------------------------------------------------------------------------
@app.route('/profresults')
def profResults():


    prof = Professor('', '', '', '', '', '', '', '')

    profid = request.args.get('profid')

    if profid is not None:
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
        prof = database.profSearch(profid)
        database.disconnect()

        titles = prof.getTitles()
        links = prof.getLinks()
        pic = prof.getPicLink()

    else:
        titles = ''
        links = ''

    html = render_template('profpage.html', prof = prof, pic = pic, titles = titles, links = links)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/resources')
def resources():
    html = render_template('resources.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/about')
def about():
    html = render_template('about.html')
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
