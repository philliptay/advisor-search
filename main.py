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

    # name = str(prof.getName())
    # areas = str(prof.getAreas()).strip('[]')
    # theses = str(prof.getTitles()).strip('[]')

    html = '<div class="row">'

    if prof.getName() != '':
        html+='<div class="col-xs-4" id="profPic">'
    # add another if to make sure get pic from dict is not null
        if pic != None:
            html+='<img src='+pic+'>'
        else:
            html+='<img src="https://live.staticflickr.com/65535/49189707262_510e60d7d6_n.jpg">'

        # open contact modal button
        html+='<button type="button" class="btn btn-info" data-toggle="modal" data-target="#contactModal">Contact</button>'
        # contact modal contents
        html+='<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="contactModalLabel" aria-hidden="true">'
        html+='<div class="modal-dialog" role="document">'
        html+='<div class="modal-content">'
        html+='<div class="modal-header">'
        html+='<h5 class="modal-title" id="contactModalLabel">Advisor Email Builder</h5>'
        html+='<button type="button" class="close" data-dismiss="modal" aria-label="Close">'
        html+='<span aria-hidden="true">&times;</span>'
        html+='</button>'
        html+='</div>'
        html+='<div class="modal-body">'
        html+='<p>Hi there</p>'
        html+='</div>'
        html+='<div class="modal-footer">'
        html+='<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>'
        html+='<button type="button" class="btn btn-primary">Send Email</button>'
        html+='</div>'
        html+='</div>'
        html+='</div>'
        html+='</div>'
        html+='</div>'
        html+='<div class="col-xs-8">'

        html+='<h3>'+str(prof.getName())+'</h3>'
        html+='<p>'+str(prof.getContact())+'</p>'
        html+='<p>'+str(prof.getBio())+'</p>'

        html+='</div></div>'
        html+='<div class="row">'

        # onclick="createForm('+str(prof.getName()) + ',' + str(prof.getAreas()).strip('[]') + ',\'' + str(prof.getTitles()).strip('[]')'+);"
        html+='<h4>Research Areas:</h4><ul>'
        for area in prof.getAreas():
            html+='<li>'+str(area[0].strip('. '))+'</li>'
        html+='</ul></div>'

        html+='<div class="row">'
        html+='<h4>Current Projects:</h4>'
        if prof.getProjects() == 'No projects found.':
            html+='<p>'+prof.getProjects()+'</p>'
        else:
            html+='<ul>'
            for proj in prof.getProjects():
                html+='<li>'+str(proj[0].strip('. '))+'</li>'
            html+='</ul>'
        html+='</div>'

        html+='<div class="row">'
        html+='<h4>Past Theses Advised:</h4>'
        if links == '':
            html+='<p>'+str(titles)+'</p>'
        else :
            html+='<ul>'
            for i in range(len(titles)):
                html+='<li><a href='+links[i].strip(', ')+' target="_blank">'+titles[i].strip(',. ')+'</li></a>'
            html+='</ul>'
        html += '</div>'

    html.encode('utf-8')
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
