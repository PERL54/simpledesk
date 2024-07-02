from app import app
from utils import checkLogin
from flask import request, session, redirect, url_for, render_template


@app.route("/register", methods = ['POST', 'GET'])
def register():
	error = None
	if request.method == 'POST': 
		if checkLogin(request):
			session['isAdmin'] = True
			return redirect(url_for('index'))
		else:
			error = 'Incorrect login data!'
	return render_template('register.html', error = error)