from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Flask from Scratch - v0.0 : Getting Started"


