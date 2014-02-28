from HuskyClassMiner import ClassMiner

print ('This is a testing utility for the ClassNames object in the UWMetaClass API.')

url = raw_input('Please enter a URL to be parsed: ')

cn = ClassMiner(url)

cn.getClasses()

cn.toString()

print(cn.length())

print(cn.containsClass('math125'))
