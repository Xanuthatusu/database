# Anthony George
# anthony.george@dixiesuccess.org
# 2015
# 
# Class that stores all the data and runs functions for the 
# gtkgui class to display using sqlite
#
#
# October 9, 2015: Anthony George
# 	fully implement sqlite3

# importing the required modules
import sqlite3

# declaring the data class to store and manipulate data using sqlite
class Data:

	# initiates the class with a self.lib variable
	def __init__(self):
		self.dbconn = sqlite3.connect("database.db")
		self.db = self.dbconn.cursor()
		self.db.execute("CREATE TABLE IF NOT EXISTS users (ID TEXT, firstName TEXT, lastName TEXT, phoneNumber TEXT, email TEXT)")
		#self.db.execute("INSERT INTO users(ID, firstName, lastName, phoneNumber, email) VALUES('ant', 'Anthony', 'George', '9032715281', 'pategeorge12@gmail.com')")
		self.dbconn.commit()
		self.reset()

	# adds data to self.lib
	def add(self, key, value):
		self.db.execute("INSERT INTO users(ID, firstName, lastName, phoneNumber, email) VALUES(?, ?, ?, ?, ?)",
			(value[0][0:3], value[0], value[1], value[2], value[3]))
		self.dbconn.commit()
		self.reset()

	# lists all the rows in the database (used mainly for debugging)
	def reset(self):
		self.userList = []
		for row in self.db.execute("SELECT * FROM users"):
			self.userList.append(row)

	# removes data from self.lib
	def remove(self, key):
		self.db.execute("DELETE FROM users WHERE firstName = ?", (key,))
		self.dbconn.commit()
		self.reset()