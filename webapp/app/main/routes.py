from flask import current_app, render_template, redirect, url_for, request
import random, logging

from app import db
from app.main import bp
from app.models import *
from app.main.forms import MyTable_Form
from app.main.boot import *

# logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index():

    mytableform = MyTable_Form()

    templateData = {
        'title' : 'Flask from Scratch',
        'section' : 'v2.0 : Running Docker Containers',
        'loc_var_01' : current_app.config['LOC_VAR_01'],
        'app_version' : current_app.config['APP_VERSION'],
        'mytable_rows' : MyTable.query.all(),
        'form' : mytableform
    }

    if request.method == 'POST':
     
        button = request.form.get('button')
        if button == 'add2db':
            new_row = MyTable(item=f'newdata_{MyTable.query.count()+1}', value=random.uniform(0, 10))
            db.session.add(new_row)
            db.session.commit()
            
        elif button == 'erasedb':
            data = MyTable.query.all()
            for i in data:
                db.session.delete(i)
            db.session.commit()

        elif button == 'submit':
            item = request.form.get('item')
            value = request.form.get('value')
            
            logging.debug(item)
            logging.debug(value)
            
            new_row = MyTable(item=mytableform.item.data, value=float(mytableform.value.data))
            db.session.add(new_row)
            db.session.commit()


        templateData = {
            'mytable_rows' : MyTable.query.all()
        }

        
        return render_template('index_mytable.html', **templateData)
    
    return render_template('index.html', **templateData)

@bp.route('/media', methods=['GET', 'POST'])
def media():

    templateData = {
        'title' : 'Another Page Style',
        'section' : 'v2.0 : Running Docker Containers',
        'loc_var_01' : current_app.config['LOC_VAR_01'],
        'app_version' : current_app.config['APP_VERSION']
    }

    return render_template('media.html', **templateData)

