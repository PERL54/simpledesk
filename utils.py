from flask import request

def checkLogin(request):
	if request.form['username'] == 'perl' and request.form['passwd'] == 'admin':
		return True
	else:
		return False