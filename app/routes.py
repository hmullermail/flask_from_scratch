from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    
    templateData = {
        'title' : 'Flask from Scratch',
        'section' : 'v0.2 : Adding a Configuration File',
        'loc_var_01' : app.config['LOC_VAR_01'],
        'app_version' : app.config['APP_VERSION']
    }

    return render_template('index.html', **templateData)

