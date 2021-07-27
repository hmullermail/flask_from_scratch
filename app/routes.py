from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Flask from Scratch - v0.1 : Simple Multiple Files Project"

