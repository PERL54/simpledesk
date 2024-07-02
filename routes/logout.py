from app import app, db
from flask import request, session, redirect, url_for, render_template


@app.route("/logout")
def logout():
	if session['isAdmin']:
		session.pop('isAdmin')
	return redirect(url_for('index'))