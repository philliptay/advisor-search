from __future__ import print_function
import sys
from sys import argv, stderr, stdout
from database import Database
from professor import Professor
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template

app = Flask(__name__, template_folder='templates')

#-------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # retrieve info from checkbox
        formInfo = ['', '', '', '', '', '', '', '', '', '', '']
        areas = request.form.getlist('area')
        print(areas)

    # areas = request.form.get('area')
    # if areas is not None:
    #     print(areas, file=sys.stderr)

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
