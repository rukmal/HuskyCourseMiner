'''
Author: Rukmal Weerawarana
Description: HuskyCourseMiner is an API to interact with the UW Course Catalog.
'''

import urllib
from bs4 import BeautifulSoup

class CourseMiner(object):
	COURSE_CATALOG_URL = "https://www.washington.edu/students/crscat/" #UW course catalog url

	"""
	Constructor for the CourseMiner object.

	Takes no parameters.
	"""
	def __init__(self):
		self.__page = BeautifulSoup(urllib.urlopen(self.COURSE_CATALOG_URL).read())
		self.__classes = dict()
		self.__size = 0

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

	"""
	Private function to get and return the course description text from a string
	of HTML syntax. Takes input in the form of a BeautifulSoup object.

	Returns a string with no leading or trailing spaces with the course title.
	"""
	def __getTitle(self, descr):
		description = str(descr)
		output = ""
		for i in range(len(description) - 1, -1, -1):
			if description[i] == '<':
				while description[i - 1] != '>':
					output = output + description[i - 1]
					i = i - 1
				break
		output = output[1:len(output) - 1] #removing leading and trailing spaces
		output = output[::-1] #reversing the output
		return output

	"""
	Constructs a dictionary of all of the classes listed
	on the UW catalog, along with the class title.

	This function only works with the UW Course Catalog.
	"""
	def getClasses(self):
		for link in self.__page.find_all('a'):
			try:
				childLink = self.COURSE_CATALOG_URL + link['href']
				childPage = BeautifulSoup(urllib.urlopen(childLink).read())
				for description in childPage.find_all('b'):
					className = description.find_all('a')[0]
					try:
						sln = self.__getClassCode(className['name'])
						classNo = int(sln[1])
						if sln[1] != "":
							if not sln[0] in self.__classes:
								self.__classes[sln[0]] = {classNo:self.__getTitle(description)}
								self.__size += 1
							else:
								if not int(sln[1]) in self.__classes[sln[0]]:
									self.__classes[sln[0]][classNo] = self.__getTitle(description)
									self.__size += 1
					except:
						pass
			except:
				pass

	"""
	Takes input in the form XXX 999, where XXX is the class title
	and 999 is the class number

	Function that returns true if a class exists, and false otherwise.
	"""
	def containsClass(self, sln):
		breakdown = self.__getClassCode(sln)
		for depID in self.__classes:
			if breakdown[0] == depID:
				for classID in self.__classes[breakdown[0]]:
					if classID == int(breakdown[1]):
						return True
		return False

	'''
	Takes input in the form of XXXm where XXX is the class title

	Function that returns a sorted list of all of the classes within a given department.
	Throws a KeyError if the department is not found.
	'''
	def getDepartmentClasses(self, department):
		output = []
		for classID in self.__classes[department.upper()]:
			output.append(classID)
		return sorted(output)


	'''
	Takes input in the form XXX 999, where XXX is the class title
	and 999 is the class number.

	Function that returns the description of a class. Throws a KeyError
	if the class is not found.
	'''
	def getTitle(self, sln):
		breakdown = self.__getClassCode(sln)
		return self.__classes[breakdown[0]][int(breakdown[1])]

	'''
	Overrides the default str method to print out formatted data from the UW course catalog.

	WARNING: The output from this method will be extremely long.
	'''
	def __str__(self):
		output = ""
		for department in self.__classes:
			output += 'Department: ' + department + '\n'
			for classNo in self.__classes[department]:
				output += '\t' + 'ID: ' + str(classNo) + '\n'
				output += '\t' + 'Title: ' + self.__classes[department][classNo] + '\n\n'
			output += '\n\n'
		return output

	'''
	Returns the number of classes in the UW course catalog.
	'''
	def length(self):
		return self.__size
