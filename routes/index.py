from app import app
from flask_login import current_user
from flask import session, render_template


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', user = current_user)