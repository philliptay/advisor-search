from sys import argv
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template

app = Flask(__name__, template_folder='.')

#-------------------------------------------------------------------------------

@app.route('/')
@app.route('/index')
def index():

    html = ''
    html += '<p>hello Dondo</p>'


    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
