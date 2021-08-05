from flask import jsonify, request, url_for, current_app
from app import db
from app.models import MyTable 
from app.api import bp

import sys, os, pathlib


@bp.route('/data', methods=['GET'])
def data():
    t = MyTable.query.all()
    table_data = {}
    for i in t:
        table_data['{:%d/%m/%Y %H:%M:%S}'.format(i.stamp)] = i.value
    
    return jsonify(table_data)


@bp.route('/system', methods=['GET'])
def system():
    system_info = {}
    system_info['Platform System'] = sys.platform
    system_info['OS Name'] = os.name
    system_info['Pathlib absolute'] = '/'.join(str(pathlib.Path().absolute()).split("\\"))    
    
    return jsonify(system_info)