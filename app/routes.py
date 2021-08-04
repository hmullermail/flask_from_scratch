from flask import render_template, redirect, url_for, request
import random, logging
from app import app
from app import db
from app.models import *
from app.forms import MyTable_Form

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    mytableform = MyTable_Form()

    templateData = {
        'title' : 'Flask from Scratch',
        'section' : 'v0.4 : Adding a Form',
        'loc_var_01' : app.config['LOC_VAR_01'],
        'app_version' : app.config['APP_VERSION'],
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

