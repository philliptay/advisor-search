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
    #     logState = 'Login'
    #     logLink = '/login'
    #     session['profs'] = None
    #     html = render_template('login.html', logState = logState, logLink = logLink)
    #     response = make_response(html)
    #     return(response)

    # username = session['username']
    # logState = 'Logout'
    # logLink = '/logout'
    # html = render_template('index.html', user=username, logState = logState, logLink = logLink)
    # response = make_response(html)
    # return(response)

    username = ''
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
        html += '<a href="#" onclick="getProfResults('+str(prof[2])+');"><li class="list-group-item" tabindex="0"><div class="flex-container-row"><div class="flex-item-stretch truncate"><strong>'+str(prof[0])+'</strong></div><div class="flex-item-rigid"><i data-toggle="tooltip" data-original-title="Click to favorite" class="fa fa-heart fav-icon"></i></div></div><br><span>Top Areas: '+ topAreas +'</span></li></a>'
    html += '</ul></div>'
    html.encode('utf-8')
    response = make_response(html)

    return(response)

#-------------------------------------------------------------------------------
@app.route('/profresults')
def profResults():


    prof = Professor('', '', '', '', '', '', '', '')

    profid = request.args.get('profid')

    database = Database()
    database.connect()
    prof = database.profSearch(profid)
    database.disconnect()

    titles = prof.getTitles()
    links = prof.getLinks()
    pic = prof.getPicLink()

    html = render_template('profpage.html', prof = prof, pic = pic, titles = titles, links = links)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------
@app.route('/emailresults')
def emailResults():

    year = request.args.get('year')
    type = request.args.get('type')
    areas = request.args.getlist('areas')
    if len(areas) > 1:
        for area in areas[:-1]:
            areasFormatted += area
            areasFormatted += ", "
        areasFormatted += ", and "
        areasFormatted += areas[-1]
    else:
        areasFormatted = areas[0]

    projs = request.args.getlist('projs')
    projFormatted = ""
    for word in projs:
        projFormatted += word


    body1 = "Dear Professor "
    body2 = "I am a " + str(year) + " in the Computer Science department and I am exploring areas of research to do my " + str(type) + ". In this search process, I reviewed academic work in " + str(areasFormatted) + "and found " + str(projFormatted) + " to be a fascinating project."
    body3 = "     Specifically… ******** in this section, discuss something in the paper that excites you. This could be something that you want to build off of in your own project, or something you hope to work on in the future. Feel free to talk personally about why you might want to work in this area. ********"
    body4 = "     Your work in " + str(areasFormatted) + " is inspiring and I would be honored if you advised me for my " + str(type) + ". Please let me know if I can send you information about myself, or if there are other steps that I should take."
    body5 = "     Sincerely,"
    body6 = "     (Your name here)"

    subject = "Request for you to be my Advisor"

    #build email body here
    html = render_template('emailpage.html', subject = subject, body1 = body1, body2 = body2, body3 = body3, body4 = body4, body5 = body5, body6 = body6)
    response = make_response(html)
    return(response)
#-------------------------------------------------------------------------------

@app.route('/resources')
def resources():
    if 'username' not in session:
        logState = 'Login'
        logLink = '/login'
    else:
        logState = 'Logout'
        logLink = '/logout'

    html = render_template('resources.html', logState = logState, logLink = logLink)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/about')
def about():
    if 'username' not in session:
        logState = 'Login'
        logLink = '/login'
    else:
        logState = 'Logout'
        logLink = '/logout'

    html = render_template('about.html', logState = logState, logLink = logLink)
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
