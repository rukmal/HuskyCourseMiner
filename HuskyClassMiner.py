import urllib
from bs4 import BeautifulSoup
from pymongo import MongoClient

class ClassMiner(object):
	"""
	Initializer for the ClassMiner object.

	Takes a url as a prarameter.
	"""
	def __init__(self, timeSchedURL):
		self.url = timeSchedURL
		self.page = BeautifulSoup(urllib.urlopen(self.url).read())
		self.classes = dict()
		self.size = 0
		self.client = MongoClient('localhost', 27017)

	"""
	Private function to split a string into its department abbreviation and course
	(if possible).

	Returns an list of size 2 with the first position being the characters in the input
	string and the second position being the numbers in the input string.
	output = [string (department ID), int (course number)]
	"""
	def __getClassCode(self, name):
		sln = []
		slnNo = ""
		slnName = ""
		for letter in name:
			try:
				int(letter)
				slnNo += letter
			except ValueError:
				slnName += letter
		sln.append(slnName.upper())
		sln.append(slnNo)
		return sln

	def __insertDB(self, sln):
		print('hi')

	"""
	Constructs and returns a dictionary of all of the classes listed
	on the website.

	This program currently works with the UW Course Catalog, and all
	TimeSchedule pages.
	"""
	def getClasses(self):
		classes = []
		for link in self.page.find_all('a'):
			try:
				childLink = 'https://www.washington.edu/students/crscat/' + link['href']
				childPage = BeautifulSoup(urllib.urlopen(childLink).read())
				for className in childPage.find_all('a'):
					try:
						sln = self.__getClassCode(className['name'])
						if sln[1] != "":
							if not sln[0] in self.classes:
								self.classes[sln[0]] = [int(sln[1])]
								self.size += 1
							else:
								if not int(sln[1]) in self.classes[sln[0]]:
									self.classes[sln[0]].append(int(sln[1]))
									self.size += 1
					except:
						pass
				for classTitle in childPage.find_all('b'):
					analyze = BeautifulSoup(classTitle)
					print(analyze.br.string)
			except:
				pass

	"""
	Takes input in the form XXX 999, where XXX is the class title,
	and 999 is the class number

	Function that returns true if a class exists, and false otherwise.
	"""
	def containsClass(self, sln):
		for classSln in self.classes:
			if sln == classSln:
				return True
		return False
	'''
	Prints out the array of classes.
	'''
	def toString(self):
		print(self.classes)

	'''
	Returns the number of classes in the current data set.
	'''
	def length(self):
		return self.size
