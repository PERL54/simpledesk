from app import app, db, User
from flask import request, session, redirect, url_for, render_template
from flask_login import login_user
import bcrypt


@app.route("/login", methods = ['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST': 
		email = request.form['email']
		password = request.form['passwd']
		print(password.encode('utf-8'))

		user_data = db.get_user_by_email(email)

		if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[3]):
			user = User(*user_data)
			login_user(user)
			return redirect('index')
		else:
			return redirect('login', error = error)
		
	return render_template('login.html', error = error)