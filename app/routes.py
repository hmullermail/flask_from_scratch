from flask import render_template, redirect, url_for, request
import random
from app import app
from app import db
from app.models import *

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        button = request.form['button']
        if button == 'add2db':
            new_row = MyTable(item=f'newdata_{MyTable.query.count()+1}', value=random.uniform(0, 10))
            db.session.add(new_row)
            db.session.commit()
            templateData = {
                'mytable_rows' : MyTable.query.all()
            }

        elif button == 'erasedb':
            data = MyTable.query.all()
            for i in data:
                db.session.delete(i)
            db.session.commit()
            templateData = {
                'mytable_rows' : MyTable.query.all()
            }

        return render_template('index_mytable.html', **templateData)
    
    templateData = {
        'title' : 'Flask from Scratch',
        'section' : 'v0.3 : Adding a Database',
        'loc_var_01' : app.config['LOC_VAR_01'],
        'app_version' : app.config['APP_VERSION'],
        'mytable_rows' : MyTable.query.all()
    }

    return render_template('index.html', **templateData)

