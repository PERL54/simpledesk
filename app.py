from flask import Flask 
from flask_login import LoginManager, UserMixin
import dbase
import os 
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days = 31)

db = dbase.DBase('database/database.db')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from routes import *


class User(UserMixin):
	def __init__(self, id, username, email, password, registration_date):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.registration_date = registration_date

	@staticmethod
	def get(user_id):
		user_data = db.get_user_by_id(user_id)
		if user_data:
			return User(*user_data)
		return None

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)

if __name__ == '__main__':
	app.run(debug = True)