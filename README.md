#HuskyCourseMiner
##Description
HuskyCourseMiner is a python utility that allows a user to scrape data from the UW Course Catalog. It works by leveraging the unique way in which the University of Washington structures its course sites, and hence only works with the current (as of March 2014) course catalog.

This utility gets data such as the number of credits and class titles directly from the main [UW course catalog](http://www.washington.edu/students/crscat/). This data is refreshed each time the program is run to ensure that the latest data is available.

This utility was written, tested and is guaranteed to work with Python 2.7.6. This utility uses BeautifulSoup to manipulate the html files, which can be installed from [here](http://www.crummy.com/software/BeautifulSoup/). To retrieve the HTML files from the UW Course Catalog, this API uses the built in Python [urllib](http://docs.python.org/2/library/urllib.html) API.

Due to the exhaustive nature of grabbing data from these sites (2 layers of nested links), the initial data grab may take up to 3 minutes depending on the speed of your internet connection and computer. After the initial grab however, the utility will be able to manipulate and access the data extremely quickly due to the efficient storage and indexing of the data using two layers of nested dictionaries. The structure of how the data is stored is discussed further in the 'structure' section of this document.

##Usage
This application is intended to be used as an API for grabbing and manipulating data from the UW course catalog. Thus, simply running the python file containing the code to grab data will not 'do' anything. To help users understand the power of this tool, I have included a testing file called HuskyClassMiner_tester.py

This program will test most of the main functions of this method, mainly grabbing data from the site, getting the title of a specific class, testing the print function and also printing the number of classes found in the course catalog.

The used should expect to see a large amount of data, as this utility prints out all of the descriptions from every single class at UW (12908 as of March 2014). Although testing most of the functionality of this program, it does not test all of it, as the API has more functions that I encourage the suer to explore.

##Structure
The HuskyCourseMiner API stores class data in the form of dictionary within a dictionary. This structure is illustrated below for convenience.
```python
{department : {classNo : description}}
```
An example of the structural storage of data is illustrated below:
```
MATH +
     |
     - 124 +
     |     |
     |     - Calculus with Analytic Geometry I (5) NW, QSR
     |
     - 125 +
     |     |
     |     - Calculus with Analytic Geometry II (5) NW
     |
     - 126 +
     |     |
     |     - Calculus with Analytic Geometry III (5) NW
```
The print function of this method also follows the same guidelines.

##Contact
This is an open source project. Contact me if you have an improvement to make and want to put in a push request.

http://rukmal.me
