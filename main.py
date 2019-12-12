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

    profPics = {
        'Aarti Gupta': 'https://live.staticflickr.com/65535/49180373052_77e070b52a_n.jpg',
        'Adam Finkelstein': 'https://live.staticflickr.com/65535/49174808528_55680f30e5_n.jpg',
        'Alan Kaplan': 'https://live.staticflickr.com/65535/49174827063_25053c72cf_n.jpg',
        'Amit Levy': 'https://live.staticflickr.com/65535/49179992102_0d98b2bb34_n.jpg',
        'Andrew Appel': 'https://live.staticflickr.com/65535/49179784736_60eaac7bde_n.jpg',
        'Arvind Narayanan': 'https://live.staticflickr.com/65535/49179784711_637259a4b4_n.jpg',
        'Barbara Engelhardt': 'https://live.staticflickr.com/65535/49179992077_74492d2c16_n.jpg',
        'Bernard Chazelle': 'https://live.staticflickr.com/65535/49179293028_bef3e4930c_n.jpg',
        'Brian Kernighan': 'https://live.staticflickr.com/65535/49179784656_afdd306907_n.jpg',
        'Christiane Fellbaum': 'https://live.staticflickr.com/65535/49179784631_705b6aa1c5_n.jpg',
        'Christopher Moretti': 'https://live.staticflickr.com/65535/49179329783_eac0ed1d8d_n.jpg',
        'Daniel Leyzberg': 'https://live.staticflickr.com/65535/49179992022_209f93deb7_n.jpg',
        'Danqi Chen': 'https://live.staticflickr.com/65535/49179292963_7c04f27026_n.jpg',
        'David August': 'https://live.staticflickr.com/65535/49179292933_c4246282e8_n.jpg',
        'David Dobkin': 'https://live.staticflickr.com/65535/49179292923_a84d098dab_n.jpg',
        'David Walker': 'https://live.staticflickr.com/65535/49179784551_8c893c24be_n.jpg',
        'Edward Felten': 'https://live.staticflickr.com/65535/49180084021_ae3a35865e_n.jpg',
        'Elad Hazan': 'https://live.staticflickr.com/65535/49180290722_4fbff02a98_n.jpg',
        'Gillat Kol': 'https://live.staticflickr.com/65535/49180084006_d8052569e9_n.jpg',
        'Iasonas Petras': 'https://live.staticflickr.com/65535/49179593928_7ec9888b7f_n.jpg',
        'Ibrahim Albluwi': 'https://live.staticflickr.com/65535/49179593918_7a0dbb089c_n.jpg',
        'Jack Brassil': 'https://live.staticflickr.com/65535/49180083976_a6d1450990_n.jpg',
        'Jaswinder Singh': 'https://live.staticflickr.com/65535/49180083951_c2548d94f4_n.jpg',
        'Jennifer Rexford': 'https://live.staticflickr.com/65535/49180083941_578ac2b7fd_n.jpg',
        'Jérémie Lumbroso': 'https://live.staticflickr.com/65535/49180083921_4ed476f389_n.jpg',
        'Jia Deng': 'https://live.staticflickr.com/65535/49180290647_89433dea8a_n.jpg',
        'Jonathan Mayer': 'https://live.staticflickr.com/65535/49180083911_9822eb3e87_n.jpg',
        'Kai Li': 'https://live.staticflickr.com/65535/49180083891_3249154470_n.jpg',
        'Karthik Narasimhan': 'https://live.staticflickr.com/65535/49180290627_398207ef13_n.jpg',
        'Kevin Wayne': 'https://live.staticflickr.com/65535/49180083871_98501dd81b_n.jpg',
        'Kyle Jamieson': 'https://live.staticflickr.com/65535/49180083851_98f7f3852b_n.jpg',
        'Larry Peterson': 'https://live.staticflickr.com/65535/49179593813_ddbc16a5fe_n.jpg',
        'Maia Ginsburg': 'https://live.staticflickr.com/65535/49180290562_ff9ebcdf3f_n.jpg',
        'Margaret Martonosi': 'https://live.staticflickr.com/65535/49180083826_f51f8a88e2_n.jpg',
        'Mark Braverman': 'https://live.staticflickr.com/65535/49179593763_aa94709bd9_n.jpg',
        'Mark Zhandry': 'https://live.staticflickr.com/65535/49179593738_3c5752df91_n.jpg',
        'Matthew Weinberg': 'https://live.staticflickr.com/65535/49180083816_d5b1dbcc24_n.jpg',
        'Michael Freedman': 'https://live.staticflickr.com/65535/49179593718_9047931257_n.jpg',
        'Mona Singh': 'https://live.staticflickr.com/65535/49180290507_a4508db633_n.jpg',
        'Olga Russakovsky': 'https://live.staticflickr.com/65535/49180083786_6c1413efdc_n.jpg',
        'Olga Troyanskaya': 'https://live.staticflickr.com/65535/49180083771_fa4848b7cb_n.jpg',
        'Ran Raz': 'https://live.staticflickr.com/65535/49179593678_72cbd10902_n.jpg',
        'Robert Dondero': 'https://live.staticflickr.com/65535/49179593663_dcb001a4b3_n.jpg',
        'Robert Fish': 'https://live.staticflickr.com/65535/49180083746_3545d49ccd_n.jpg',
        'Robert Schapire': 'https://live.staticflickr.com/65535/49180290447_35de556377_n.jpg',
        'Robert Sedgewick': 'https://live.staticflickr.com/65535/49180083736_a8d26b83b0_n.jpg',
        'Robert Tarjan': 'https://live.staticflickr.com/65535/49179593638_3bc0a2698d_n.jpg',
        'Ryan Adams': 'https://live.staticflickr.com/65535/49179593623_b11912d152_n.jpg',
        'Sanjeev Arora': 'https://live.staticflickr.com/65535/49180083696_ae484b10df_n.jpg',
        'Sebastian Seung': 'https://live.staticflickr.com/65535/49180083686_dacfb2ef3d_n.jpg',
        'Szymon Rusinkiewicz': 'https://live.staticflickr.com/65535/49180083671_f3c7999fec_n.jpg',
        'Tom Griffiths': 'https://live.staticflickr.com/65535/49179593578_43e007ccc2_n.jpg',
        'Wyatt Lloyd': 'https://live.staticflickr.com/65535/49180083646_05531b4e1a_n.jpg',
        'Xiaoyan Li': 'https://live.staticflickr.com/65535/49180083641_fa065ee330_n.jpg',
        'Yoram Singer': 'https://live.staticflickr.com/65535/49180290367_31ec461978_n.jpg',
        'Zachary Kincaid': 'https://live.staticflickr.com/65535/49180290337_a95fe9f7d5_n.jpg',
        'Zeev Dvir': 'https://live.staticflickr.com/65535/49180290322_14fc97ca95_n.jpg',
    }

    prof = Professor('', '', '', '', '', '', '')

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
        if profPics.get(prof.getName()) != None:
            html+='<img src='+str(profPics.get(prof.getName()))+'>'
        else:
            html+='<img src="https://live.staticflickr.com/65535/49189707262_510e60d7d6_n.jpg">'

        html+='</div>'
        html+='<div class="col-xs-8">'

        html+='<h3>'+str(prof.getName())+'</h3>'
        html+='<p>'+str(prof.getContact())+'</p>'
        html+='<p>'+str(prof.getBio())+'</p>'

        html+='</div></div>'
        html+='<div class="row">'
        html+='<button>Contact</button>'
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
