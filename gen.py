# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from generator import main, randomNouns, randomAdjs

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'gen.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show():
    return render_template('blank.html')

@app.route('/tavern', methods=['GET', 'POST'])
def tavern():
    error = None
    if request.method == 'POST':
        num = int(request.form['selection'])
        names = [main() for i in range(num)]
        return render_template('tavern.html', error=error, names=names)
        #return render_template('tavern.html', error=error, names=names)
    else:
        tavern = main()
        names = [tavern]
        return render_template('tavern.html', error=error, names=names)

app.run()
