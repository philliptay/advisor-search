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
    # database = Database()
    # database.connect()
    # database.insertUser('placeholder')
    # database.disconnect()
    # return redirect(url_for('index'))

    html = render_template('login.html', logState = logState, logLink = logLink)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():

    #if 'username' not in session:
    #    logState = 'Login'
    #    logLink = '/login'
    #    session['profs'] = None
    #    html = render_template('login.html', logState = logState, logLink = logLink)
    #    response = make_response(html)
    #    return(response)

    #username = session['username']
    username = 'placeholder'
    logState = 'Logout'
    logLink = '/logout'
    html = render_template('index.html', user=username, logState = logState, logLink = logLink)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/searchresults')
def searchResults():
    allAreas = ['Computational Biology,Computer Architecture,Economics/Computation,Graphics,Vision,Machine Learning,AI,Natural Language Processing,Policy,Programming Languages/Compilers,Security & Privacy,Systems,Theory']
    allAreasArray = ['Computational Biology','Computer Architecture','Economics/Computation','Graphics','Vision','Machine Learning','AI','Natural Language Processing','Policy','Programming Languages/Compilers','Security & Privacy','Systems','Theory']

    inputString = request.args.getlist('inputs')
    inputs = inputString[0].split(',')
    for input in inputs:
        if input == 'All':
            inputs = allAreasArray

    areas = []
    keywords = []

    for input in inputs:
        if input in allAreasArray:
            areas.append(input)
        else:
            keywords.append(input)

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

    resultsnum = len(profList)

    html = '<h3>Search Results ('+str(resultsnum)+')</h3><div id="resultsWrapper" class="flex-item-shrink resizable"><ul class="marginless">'
    for prof in profList:
        active = ''
        topAreas = ''
        for i in range(min(3, len(prof[1]))) :
            topAreas += prof[1][i]+', '
        topAreas = topAreas.rstrip(', ')

        # if database.isProfFavorited(username, prof[2]):
        #     active = 'active'

        html += '<div class=prof'+str(prof[2])+' onclick="getProfResults('+str(prof[2])+');"><li class="list-group-item" tabindex="0"><div class="flex-container-row"><div class="flex-item-stretch truncate"><strong>'+str(prof[0])+'</strong></div><div class="flex-item-rigid"><i data-toggle="tooltip" data-original-title="Click to favorite" class="fa fa-heart fav-icon '+active+'" onclick="getFavorited('+str(prof[2])+');"></i></div></div><br><span>Top Areas: '+ topAreas +'</span></li></div>'
    html += '</ul></div>'
    html.encode('utf-8')
    database.disconnect()
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

    html = render_template('profpage.html', profid = profid, prof = prof, pic = pic, titles = titles, links = links)
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/favoritedProf')
def favoritedProf():

    profid = request.args.get('profid')
    username = 'placeholder'

    database = Database()
    database.connect()
    database.updateFavoritedProf(username, profid)
    results = database.favoritedProfSearch(username)
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
    html = '<div class="flex-container-row">'
    html += '<h3 class="flex-item-stretch truncate">Favorite Advisors ('+str(resultsnum)+')</h3><h4 class="flex-item-rigid"><i id="fav-toggle" class="fa text-button fa-minus" onclick="toggleFavs()"></i></h4></div><div id="fav-content" class="flex-item-shrink resizable" style="max-height: 30vh;"><ul class="marginless">'
    for prof in profList:
        topAreas = ''
        for i in range(min(3, len(prof[1]))) :
            topAreas += prof[1][i]+', '
        topAreas = topAreas.rstrip(', ')
        html += '<div class=prof'+str(prof[2])+' onclick="getProfResults('+str(prof[2])+');"><li class="list-group-item" tabindex="0"><div class="flex-container-row"><div class="flex-item-stretch truncate"><strong>'+str(prof[0])+'</strong></div><div class="flex-item-rigid"><i data-toggle="tooltip" data-original-title="Click to unfavorite" class="fa fa-heart fav-icon active" onclick="getFavorited('+str(prof[2])+');"></i></div></div><br><span>Top Areas: '+ topAreas +'</span></li></div>'
    html += '</ul></div>'
    html.encode('utf-8')
    response = make_response(html)

    return(response)


#-------------------------------------------------------------------------------
@app.route('/backresults')
def backResults():
    prof = Professor('', '', '', '', '', '', '', '')

    profid = request.args.get('profid')

    database = Database()
    database.connect()
    prof = database.profSearch(profid)
    database.disconnect()

    html = '<div class="modal-header">'
    html += '<button type="button" class="close" data-dismiss="modal">&times;</button>'
    html += '<h4 class="modal-title">Advisor Email Builder</h4>'
    html += '</div>'
    html += '<div class="modal-body">'
    html += '<p>Enter the information then click generate to build a customized email to Professor ' + str(prof.getName()) + '</p>'
    html += '<form id="emailForm">'
    html += '<input type="hidden" id="profid" value=' + str(profid) + '>'
    html += '<h4>Select Class: </h4>'
    html += '<select name="year" id="year">'
    html += '<option value="Junior">Junior</option>'
    html += '<option value="Senior">Senior</option>'
    html += '</select>'
    html += '<h4>Select Project Type: </h4>'
    html += '<select name="type" id="type">'
    html += '<option value="Independent Work">Independent Work</option>'
    html += '<option value="Thesis">Thesis</option>'
    html += '</select>'
    html += '<h4>Area of Research that interests you most: </h4>'
    html += '<select name="areas" id="areas">'
    areaCount = 0
    for area in prof.getAreas():
        html += '<option value="' + str(areaCount) + '">' + str(area[0].strip('. ')) + '</option>'
        areaCount += 1
    html += '</select>'
    html += '<h4>Select the Project or Thesis that Interests you most: </h4>'
    if (prof.getProjects() == 'No projects found.') and (prof.getLinks() == ""):
        html += '<input type="text" id="projs" placeholder="Enter a project or thesis">'
    else:
        html += '<select name="projs" id="projs" style="width: 500px;">'
        projCount = 0
        if prof.getProjects() != 'No projects found.':
            for proj in prof.getProjects():
                html += '<option value="' + str(projCount) + '">' + str(proj[0].strip('. ')) + '</option>'
                projCount += 1
        if prof.getLinks() != "":
            for title in prof.getTitles():
                html += '<option value="' + str(projCount) + '">' + str(title.strip(',. ')) + '</option>'
                projCount += 1
        html += '</select>'
    html += '</form>'
    html += '</div>'
    html += '<div class="modal-footer">'
    html += '<button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>'
    html += '<input type="button" class="btn btn-primary" value="Generate" onclick="getEmailResults();"/>'
    html += '</div>'


    html.encode('utf-8')
    response = make_response(html)

    return(response)

#-------------------------------------------------------------------------------
@app.route('/emailresults')
def emailResults():
    prof = Professor('', '', '', '', '', '', '', '')

    profid = request.args.get('profid')

    database = Database()
    database.connect()
    prof = database.profSearch(profid)
    database.disconnect()

    year = request.args.get('year')
    type = request.args.get('type')
    areasNum = request.args.getlist('areas')
    areas = []
    for num in areasNum:
        areas.append(prof.getAreas()[int(num)][0].strip('. '))

    if len(areas) > 1:
        for area in areas[:-1]:
            areasFormatted += area
            areasFormatted += ", "
        areasFormatted += ", and "
        areasFormatted += areas[-1]
    else:
        areasFormatted = areas[0]

    projNum = request.args.getlist('projs')
    profProjects = prof.getProjects()

    print(projNum)

    try:
        int(projNum[0])
    except:
        print('hi')
        proj = projNum
    else:
        if int(projNum[0]) >= len(profProjects):
            proj = prof.getTitles()[int(projNum[0]) - len(profProjects)]
        else:
            proj = profProjects[int(projNum[0])][0].strip('. ')
    print(proj)
    projFormatted = ""
    for word in proj:
        projFormatted += word

    body1 = "Dear Professor " + str(prof.getName().split()[1]) + ","
    body2 = "I am a " + str(year) + " in the Computer Science department and I am exploring areas of research to do my " + str(type) + ". In this search process, I reviewed academic work in " + str(areasFormatted) + " and found " + str(projFormatted) + " to be a fascinating project."
    body3 = "Specifically… ******** in this section, discuss something in the paper that excites you. This could be something that you want to build off of in your own project, or something you hope to work on in the future. Feel free to talk personally about why you might want to work in this area. ********"
    body4 = "Your work in " + str(areasFormatted) + " is inspiring and I would be honored if you advised me for my " + str(type) + ". Please let me know if I can send you information about myself, or if there are other steps that I should take."
    body5 = "Sincerely,"
    body6 = "(Your name here)"

    subject = "Request for you to be my Advisor"

    mail = "mailto:" + str(prof.getContact()) + "?subject=" + str(subject) + "&body=" + str(body1) + "%0D%0A%0D%0A" + str(body2) + "%0D%0A%0D%0A" + str(body3) + "%0D%0A%0D%0A" + str(body4) + "%0D%0A%0D%0A" + str(body5) + "%0D%0A%0D%0A" + str(body6)


    html = '<div class="modal-header">'
    html += '<button type="button" class="close" data-dismiss="modal">&times;</button>'
    html += '<h4 class="modal-title">Advisor Email Builder</h4>'
    html += '</div>'
    html += '<input type="hidden" id="profid" value=' + str(profid) + '>'
    html += '<div class="modal-body">'
    html += '<h4>Subject:</h4>'
    html += '<p>' + str(subject) + '</p>'
    html += '<h4>Body:</h4>'
    html += '<p>' + str(body1) + '</p>'
    html += '<p>' + str(body2) + '</p>'
    html += '<p>' + str(body3) + '</p>'
    html += '<p>' + str(body4) + '</p>'
    html += '<p>' + str(body5) + '</p>'
    html += '<p>' + str(body6) + '</p>'
    html += '</div>'
    html += '<div class="modal-footer">'
    html += '<button type="button" class="btn btn-default" style="margin: 2px;" onclick="getBackResponse();">Edit Inputs</button>'
    html += '<a type="button" class="btn btn-primary" href="' + str(mail) + '">Review Email</a>'
    html += '</div>'
    html.encode('utf-8')
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
