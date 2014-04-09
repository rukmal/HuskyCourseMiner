'''
Author: Rukmal Weerawarana
Description: Testing utility for the HuskyCourseMiner API
'''

from HuskyCourseMiner import CourseMiner #importing the HuskyCourseMiner API

CourseMiner = CourseMiner() #constructing new CourseMiner object

print('Welcome to the HuskyCourseMiner API testing utility.\n')
print('Are you sure you want to fetch courses from ' + CourseMiner.COURSE_CATALOG_URL + '?')
#getting user confirmation
raw_input('Press enter to continue, or press Ctrl+Z to quit.')

CourseMiner.getClasses() #fetching classes from the UW Course catalog.

print(CourseMiner) #printing out all of the classes and titles in the course catalog

print(CourseMiner.length()) #printing out the number of classes in the catalog

print(CourseMiner.getTitle('cse331')) #printing the title of the class passed through as a parameter
