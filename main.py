from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from sys import argv

app = Flask(__name__, template_folder='.')

#-------------------------------------------------------------------------------

@app.route('/')
def index():

    html = ''
    html += '<p>hello Dondo</p>'


    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
