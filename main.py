from sys import argv
from database import Database
from professor import Professor
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template

app = Flask(__name__, template_folder='templates')

#-------------------------------------------------------------------------------

@app.route('/')
def index():

    area = request.args.get('area')
    if (area is None) or (area.strip() == ''):
        area = ''
    else:
        dept = dept.strip().lower()

    DATABASE_NAME = 'reg.sqlite'
    if not path.isfile(DATABASE_NAME):
        raise Exception('Database connection failed')
    connection = connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT profs.name, profs.contact, areas.area, profs.bio FROM areas, profs WHERE areas.profid = profs.profid AND area = \"' + area + '\"')
    rows = cursor.fetchall()

    # for row in rows:
    # add prof name to table in html code
    # pass cookies for each profs contact and bio
    # not sure how it will work for profs with multiple areas





    # database = Database()
    # database.connect()
    # results = database.search(formInfo)
    # database.disconnect()

    html = render_template('index.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
