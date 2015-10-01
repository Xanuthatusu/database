import pickle
class Users:
	def __init__(self):
		with open("dict.txt", "rb") as fp:
			#self.lib = {"Anthony": ["Anthony", "George", "96032715281", "pategeorge12@gmail.com"], "David": ["a", "A", "a", "A"]}
			self.lib = pickle.load(fp)


	def add(self, key, value):
		self.lib[key] = value

	def remove(self, key):
		del self.lib[key]

	def save(self):
		with open("dict.txt", "wb") as fp:
			pickle.dump(self.lib, fp)