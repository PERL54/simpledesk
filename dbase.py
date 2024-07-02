import sqlite3 
from datetime import datetime
import bcrypt

path = 'my_db.db'

class DBase():
	def __init__(self, pathToDbase):
		self.conn = sqlite3.connect(pathToDbase, check_same_thread=False)
		self.cursor = self.conn.cursor()
		self.createDBase()

	def createDBase(self):
		self.cursor.execute("""
					CREATE TABLE IF NOT EXISTS Users(
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						username TEXT NOT NULL UNIQUE,
						email TEXT NOT NULL UNIQUE,
						passw_hash TEXT NOT NULL,
						registration_date TEXT NOT NULL)""")

		self.conn.commit()

	def addUser(self, username, email, password):
		registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		try:
			self.cursor.execute("""
							INSERT INTO Users (username, email, passw_hash, registration_date)
							VALUES (?, ?, ?, ?)""", (username, email, password, registration_date))
		except sqlite3.IntegrityError as e:
			if 'email' in str(e):
				print('Email error!')
				return False
			elif 'username' in str(e):
				print('Username error!')
				return False

		self.conn.commit()
		return True


	def hash_password(self, password):
		salt = bcrypt.gensalt()
		hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
		return hashed_password


	def get_user_by_id(self, user_id):
		self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
		return self.cursor.fetchone()

	def get_user_by_username(self, username):
		self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
		return self.cursor.fetchone()

	def get_user_by_email(self, email):
		self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
		return self.cursor.fetchone()

	def close(self):
		self.conn.close()

