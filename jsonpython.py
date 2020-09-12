import json

#JSON in Python    Python Tutorial    Learn Python Programming
print(dir(json))
'''
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
'''
#Convert string dictionary to JSON dictionary
jsonloadsexample = """{"title":"Tron: Legacy", "composer":"Daft Punk", "releaseyear":2010, "budget":170000000, "actors":null, "wonoscar":false}"""  #triple quotes converts to string
tron = json.loads(jsonloadsexample)
print(tron) #print {'title': 'Tron: Legacy', 'composer': 'Daft Punk', 'releaseyear': 2010, 'budget': 170000000, 'actors': None, 'wonoscar': False}
print(type(tron)) #print <class 'dict'>
#Open JSON as text file
openjsonfile = open("movie1.txt","r",encoding="utf-8")
jsonfile = json.load(openjsonfile)
openjsonfile.close()
print(jsonfile) #print {'title': 'Gattaca', 'releaseyear': 1997, 'isawesome': True, 'wonoscar': False, 'actors': ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean'], 'budget': None, 'credits': {'director': 'Andrew Niccol', 'writer': 'Andrew Niccol', 'composer': 'Michael Nyman', 'cinematographer': 'Sƚawomir Idziak'}}
print(type(jsonfile)) #print <class 'dict'>
print(jsonfile["title"]) #print Gattaca
print(jsonfile["actors"]) #print ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean'] 
print(jsonfile["releaseyear"]) #print 1997
#Convert JSON dictionary to JSON string
print(json.dumps(jsonfile)) #print {"title": "Gattaca", "releaseyear": 1997, "isawesome": true, "wonoscar": false, "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"], "budget": null, "credits": {"director": "Andrew Niccol", "writer": "Andrew Niccol", "composer": "Michael Nyman", "cinematographer": "S\u019aawomir Idziak"}}
print(type(json.dumps(jsonfile))) #print <class 'str'>  RM:  notice the difference between <class 'dict'> and <class 'str'> for jsonfile object variable.
slicejsonfile = json.dumps(jsonfile)
print(slicejsonfile[10:30]) #print "Gattaca", "releasey
#Convert JSON dictionary to JSON string true text
truetextshowallcharactersnoasciionly = json.dumps(jsonfile, ensure_ascii=False)
print(truetextshowallcharactersnoasciionly) #print {"title": "Gattaca", "releaseyear": 1997, "isawesome": true, "wonoscar": false, "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"], "budget": null, "credits": {"director": "Andrew Niccol", "writer": "Andrew Niccol", "composer": "Michael Nyman", "cinematographer": "Sƚawomir Idziak"}}
#Write JSON file to a text file
jsonobjecttofile = {}  #create a JSON object create a dictionary first
jsonobjecttofile["title"] = "Minority Report"
jsonobjecttofile["director"] = "Steven Spielberg"
jsonobjecttofile["composer"] = "John Williams"
jsonobjecttofile["actors"] = ["Tom Cruise","Colin Farrell","Samantha Morton","Max von Sydow"]
jsonobjecttofile["isawesome"] = True
jsonobjecttofile["budget"] = 102000000
jsonobjecttofile["cinematographer"] = "Janusz Kami\u0144ski"
print(jsonobjecttofile) #print {'title': 'Minority Report', 'director': 'Steven Spielberg', 'composer': 'John Williams', 'actors': ['Tom Cruise', 'Colin Farrell', 'Samantha Morton', 'Max von Sydow'], 'isawesome': True, 'budget': 102000000, 'cinematographer': 'Janusz Kamiński'}
print(type(jsonobjecttofile)) #print <class 'dict'>
writejsonfile = open("movie2.txt","w",encoding="utf-8")
json.dump(jsonobjecttofile, writejsonfile, ensure_ascii=False)
writejsonfile.close()

#JSON Crash Course RM:  Finish video using Python instead of xhttp
openjsonjsonfile = open("jsoncrashcourse.json","r")
jsonfile = json.load(openjsonjsonfile)
openjsonjsonfile.close()
print(jsonfile) #print [{'name': 'Brad Traversy', 'age': 35, 'addressembeddedobject': {'street': '5 Main St', 'city': 'Boston'}, 'childenarray': ['Brianna', 'Nicholas']}, {'peoplearray': [{'name': 'Brad', 'age': 35}, {'name': 'John', 'age': 40}, {'name': 'Sara', 'age': 25}]}]
print(type(jsonfile)) #print <class 'list'>
openjsontextfile = open("jsoncrashcourse.txt","r")
jsonfile = json.load(openjsontextfile)
openjsontextfile.close()
print(jsonfile) #print [{'name': 'Brad Traversy', 'age': 35, 'addressembeddedobject': {'street': '5 Main St', 'city': 'Boston'}, 'childenarray': ['Brianna', 'Nicholas']}, {'peoplearray': [{'name': 'Brad', 'age': 35}, {'name': 'John', 'age': 40}, {'name': 'Sara', 'age': 25}]}]
print(type(jsonfile)) #print <class 'list'>
print(jsonfile[0]) #print {'name': 'Brad Traversy', 'age': 35, 'addressembeddedobject': {'street': '5 Main St', 'city': 'Boston'}, 'childenarray': ['Brianna', 'Nicholas']}
print(jsonfile[1]) #print {'peoplearray': [{'name': 'Brad', 'age': 35}, {'name': 'John', 'age': 40}, {'name': 'Sara', 'age': 25}]}
print(type(jsonfile[1])) #print <class 'dict'>
print(jsonfile[1]["peoplearray"]) #print [{'name': 'Brad', 'age': 35}, {'name': 'John', 'age': 40}, {'name': 'Sara', 'age': 25}]
print(type(jsonfile[1]["peoplearray"])) #print <class 'list'>
print(jsonfile[1]["peoplearray"][2]) #print {'name': 'Sara', 'age': 25}
print(type(jsonfile[1]["peoplearray"][2])) #print <class 'dict'>
print(jsonfile[1]["peoplearray"][2]["age"]) #print 25

#Python Tutorial Working with JSON Data using the json Module
import json
#Convert string to Python object.
#people is the key.  The value of the array is two objects.  Each objects has four keys name, phone, emails, haslicense.  Why peoplestring needs triple single-quotes? 
peoplestring = '''{"people":[{"name":"John Smith", "phone":"615-555-7164", "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"], "haslicense":true}, {"name":"Jane Doe", "phone":"560-555-5153", "emails":null, "haslicense":true}]}'''
loadtopython = json.loads(peoplestring)
print(loadtopython) #print {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@bogusemail.com', 'john.smith@work-place.com'], 'haslicense': True}, {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'haslicense': True}]}
print(type(loadtopython)) #print <class 'dict'>.  Loading json object to Python it becomes a dictionary by default.
#https://docs.python.org/3/library/jsonhtml#encoders-and-decoders a list of json and what Python converts to.  Another example json array to Python it becomes a list.
print(type(loadtopython["people"])) #print <class 'list'>
for sinceitsalist in loadtopython["people"]:
	print(type(sinceitsalist)) #print <class 'dict'>\n <class 'dict'>
	print(sinceitsalist) #print {'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@bogusemail.com', 'john.smith@work-place.com'], 'haslicense': True}\n {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'haslicense': True}
	print(sinceitsalist["name"]) #print John Smith\n Jane Smith
for deletephone in loadtopython["people"]:
	del deletephone["phone"]
print(peoplestring) #print {"people":[{"name":"John Smith", "phone":"615-555-7164", "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"], "haslicense":true}, {"name":"Jane Doe", "phone":"560-555-5153", "emails":null, "haslicense":true}]}
removephone = json.dumps(peoplestring) #convert Python object to string
print(type(removephone)) #print <class 'str'>
print(removephone) #print "{\"people\":[{\"name\":\"John Smith\", \"phone\":\"615-555-7164\", \"emails\":[\"johnsmith@bogusemail.com\",\"john.smith@work-place.com\"], \"haslicense\":true}, {\"name\":\"Jane Doe\", \"phone\":\"560-555-5153\", \"emails\":null, \"haslicense\":true}]}"
removephonecorrect= json.dumps(loadtopython)
print(removephonecorrect) #print {"people": [{"name": "John Smith", "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"], "haslicense": true}, {"name": "Jane Doe", "emails": null, "haslicense": true}]}
removephonecorrectindent= json.dumps(loadtopython, indent=2, sort_keys=True)
print(removephonecorrectindent)
'''
{
  "people": [
    {
      "emails": [
        "johnsmith@bogusemail.com",
        "john.smith@work-place.com"
      ],
      "haslicense": true,
      "name": "John Smith"
    },
    {
      "emails": null,
      "haslicense": true,
      "name": "Jane Doe"
    }
  ]
}
'''
#Load JSON files and Python objects and write objects back to JSON files
#First, a self-discovered lesson on triple quotes.
#Add triple quotes because TypeError: the JSON object must be str, bytes or bytearray, not 'dict'
statesareacodes = '''{"states":[{"name":"Alabama","abbreviation":"AL","area_codes":["205","251","256","334","938"]},{"name":"Alaska","abbreviation":"AK","area_codes":["907"]},{"name":"Arizona","abbreviation":"AZ","area_codes":["480","520","602","623","928"]},{"name":"Arkansas","abbreviation":"AR","area_codes":["479","501","870"]},{"name":"California","abbreviation":"CA","area_codes":["209","213","310","323","408","415","424","442","510","530","559","562","619","626","628","650","657","661","669","707","714","747","760","805","818","831","858","909","916","925","949","951"]},{"name":"Colorado","abbreviation":"CO","area_codes":["303","719","720","970"]},{"name":"Connecticut","abbreviation":"CT","area_codes":["203","475","860","959"]}'''
loadstatestopython = json.loads(statesareacodes)
print(loadstatestopython) #print {'states': [{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}, {'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}, {'name': 'Arizona', 'abbreviation': 'AZ', 'area_codes': ['480', '520', '602', '623', '928']}, . . .
print(type(loadstatestopython)) #print <class 'dict'>
#Load JSON files and Python objects and write objects back to JSON files
with open("states.json") as fileobject:
	pythonobjectdata = json.load(fileobject)
print(pythonobjectdata) #print {'states': [{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}, {'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}, {'name': 'Arizona', 'abbreviation': 'AZ', 'area_codes': ['480', '520', '602', '623', '928']}, . . .
print(type(pythonobjectdata)) #print <class 'dict'>
for state in pythonobjectdata["states"]:
	print(state) #print {'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}\n {'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}\n . . .
for state in pythonobjectdata["states"]:
	print(state["name"]+", "+state["abbreviation"]) #print Alabama, AL\n Alaska, AK\n . . .
#delete area codes from pythonobjectdata
for deleteareacodes in pythonobjectdata["states"]:
	del deleteareacodes["area_codes"]
#The dump method converts the data to JSON file.  The dumps method converts the data to JSON string.
stringstates = json.dumps(pythonobjectdata)
print(stringstates) #print {"states": [{"name": "Alabama", "abbreviation": "AL"}, {"name": "Alaska", "abbreviation": "AK"}, {"name": "Arizona", "abbreviation": "AZ"}, . . .
#Create new JSON file newstates.json
with open("newstates.json","w") as fileobject:
	json.dump(pythonobjectdata, fileobject, indent=2)
'''
#Another example.  Download JSON data from an API.  Converts dollars to another currency at Yahoo.  Unfortunately, the link doesn't work.  I do my best.  Comment the example.
from urllib.request import urlopen
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
	source = response.read()
print(source) #prints content of website as a string
data = json.loads(source) #convert source as a string to a Python object as the variable data
print(len(data["list"]["resources"])) #count the number of resources contents inside the list list
conversionratesdictionary = dict()
for eachforeigncurrencyconversion in data["list"]["resources"]:
	print(eachforeigncurrencyconversion)
	foreigncountry = eachforeigncurrencyconversion["resource"]["fields"]["name"]
	usdconversionnumber = eachforeigncurrencyconversion["resource"]["fields"]["price"]
	print(foreigncountry, price) #print USD/ALL 113.230003 #RM:  it's one example.
	conversionratesdictionary[foreigncountry] = usdconversionnumber
print(conversionratesdictionary["USD/EUR"]) #print 0.846500
readjsonbetter = json.dumps(data, indent=2)
print(readjsonbetter)
'''

#What Is JSON JSON Crash Course
#There are five key-value pairs.  Objects are wrapped by curly braces; a combination of key value pairs.  Keys are strings.  Values are numbers, strings, objects, or arrays.  Arrays are wrapped by square brackets.  Arrays are multiple values for the same key.  In particular, streetaddress, city, state, and zip are an object for address.  phonenumber is an array with two objects home and fax phone numbers.
example = {"firstname":"John", "lastname":"Smith", "age":25, "address":{"streetaddress":"21 2nd Street", "city":"New York", "state":"NY", "zip":"10021"}, "phonenumber":[{"type":"home", "number":"212 555-1234"}, {"type":"fax","number":"646 555-4567"}]}
print(example) #print {'firstname': 'John', 'lastname': 'Smith', 'age': 25, 'address': {'streetaddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'zip': '10021'}, 'phonenumber': [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]}
print(type(example)) #print <class 'dict'>
examplestring = '''{"firstname":"John", "lastname":"Smith", "age":25, "address":{"streetaddress":"21 2nd Street", "city":"New York", "state":"NY", "zip":"10021"}, "phonenumber":[{"type":"home", "number":"212 555-1234"}, {"type":"fax","number":"646 555-4567"}]}'''
print(examplestring) #print {"firstname":"John", "lastname":"Smith", "age":25, "address":{"streetaddress":"21 2nd Street", "city":"New York", "state":"NY", "zip":"10021"}, "phonenumber":[{"type":"home", "number":"212 555-1234"}, {"type":"fax","number":"646 555-4567"}]}
print(type(examplestring)) #print <class 'str'>
stringtojson = json.loads(examplestring)
print(stringtojson) #print {'firstname': 'John', 'lastname': 'Smith', 'age': 25, 'address': {'streetaddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'zip': '10021'}, 'phonenumber': [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]}
print(type(stringtojson)) #print <class 'dict'>
print(stringtojson["address"]) #print {'streetaddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'zip': '10021'}
print(stringtojson["address"]["city"]) #print New York
print(stringtojson["phonenumber"]) #print [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]
print(type(stringtojson["phonenumber"])) #print <class 'list'>
#print(stringtojson["phonenumber"]["type"]) #print TypeError: list indices must be integers or slices, not str
for eachtype in stringtojson["phonenumber"]:
	print(eachtype["type"]) #print home\n fax

#Python Tutorial for Beginners 43 - Working With JSON Data in Python
awhatever = {"name":"max", "age":22, "marks": [90, 50, 80, 40], "pass":True}
print(type(awhatever)) #print <class 'dict'>
print(json.dumps(awhatever)) #print {"name": "max", "age": 22, "marks": [90, 50, 80, 40], "pass": true}
print(json.dumps(awhatever, separators=(". ","="))) #print {"name"="max". "age"=22. "marks"=[90. 50. 80. 40]. "pass"=true}
print(json.dumps({"name":"max", "age":22})) #print {"name": "max", "age": 22}
print(json.dumps(["1", "2"])) #print ["1", "2"]
print(json.dumps(("1", "2"))) #print ["1", "2"]
print(json.dumps("Hello World")) #print "Hello World"
print(json.dumps(100)) #print 100
print(type(json.dumps(100))) #print <class 'str'>
print(json.dumps(15.56)) #print 15.56
print(json.dumps(False)) #print false
print(json.dumps(True)) #print true
print(json.dumps(None)) #print null
with open("saveasjsonfile.json","w") as fileobject:
	fileobject.write(json.dumps(awhatever))
fileobject.close()
with open("saveasjsonfile.json","r") as fileobject2:
	print(fileobject2.read()) #print {"name": "max", "age": 22, "marks": [90, 50, 80, 40], "pass": true}
	print(type(fileobject2.read())) #print <class 'str'>
	#print(json.loads(fileobject2.read())) #print json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
	givemethestring = fileobject2.read()
	print(givemethestring) #print null
	jsonstring = fileobject2.read()
	#jsonvalue = json.loads(jsonstring)
	#print(type(jsonvalue)) #print json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#The tutorial doesn't work.  A prior tutorial works.
openjsonjsonfile = open("saveasjsonfile.json","r")
jsonfile = json.load(openjsonjsonfile)
print(jsonfile) #print {'name': 'max', 'age': 22, 'marks': [90, 50, 80, 40], 'pass': True}
print(type(jsonfile)) #print <class 'dict'>
openjsonjsonfile.close()
print(jsonfile["name"]) #print max

#Python - Accessing Nested Dictionary Keys
with open("source-data.json") as accessjson:
    readcontent = json.load(accessjson) #create a python object with .json file
print(type(readcontent)) #print <class 'dict'>
print(readcontent)
'''
{'results': [{'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Daniel Weat'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Bernd Raucher'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}]}
'''
print(readcontent["results"])
'''
[{'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Daniel Weat'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}, {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Bernd Raucher'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}]
'''
accessquestion = readcontent["results"]
print(type(accessquestion)) #print <class 'list'>
#print(accessquestion["course"]) #print error message TypeError: list indices must be integers or slices, not str
#RM:  JSON is list items are dictionaries.  Accessing nested dictionaries and lists--a dictionary contains a list contains a dictionary contains a list.
print(type(accessquestion[1]))
print(accessquestion[1]) #print <class 'dict'>
'''
{'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Daniel Weat'}}]}
'''
for eachaccessquestion in accessquestion:
    print(eachaccessquestion)
    '''
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Daniel Weat'}}]}
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Daniel Weat'}}]}
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Mike Jauranol'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}
    {'_class': 'question', 'course': {'_class': 'course', 'title': 'Angular 7 (formerly Angular 2) - The Complete Guide', 'url': '/the-complete-guide-to-angular-2/'}, 'replies': [{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Bernd Raucher'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]}
    '''
print(type(eachaccessquestion)) #print <class 'dict'>
accessrepliesdictionarykey = eachaccessquestion["replies"]
print(type(accessrepliesdictionarykey))  #print <class 'list'>
print(accessrepliesdictionarykey)  #RM:  it printed the last replies in the for loop for eachaccessquestion in accessquestion:
'''
[{'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Bernd Raucher'}}, {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}]
'''
for eachaccessrepliesdictionarykey in accessrepliesdictionarykey:
    print(eachaccessrepliesdictionarykey)
    '''
    {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}
    {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Bernd Raucher'}}
    {'_class': 'answer', 'user': {'_class': 'user', 'display_name': 'Maximilian Schwarzmueller'}}
    '''
print(type(eachaccessrepliesdictionarykey)) #print <class 'dict'>
username = eachaccessrepliesdictionarykey["user"]["display_name"]
print(username) #print Maximilian Schwarzmueller
def getusernames():
    accessquestion = readcontent["results"]
    for eachaccessquestion in accessquestion:
        accessrepliesdictionarykey = eachaccessquestion["replies"]
        for eachaccessrepliesdictionarykey in accessrepliesdictionarykey:
            username = eachaccessrepliesdictionarykey["user"]["display_name"]
            print(username)
            savedatalist.append(username)
savedatalist = []
getusernames()
'''
Maximilian Schwarzmueller
Maximilian Schwarzmueller
Maximilian Schwarzmueller
Daniel Weat
Maximilian Schwarzmueller
Mike Jauranol
Mike Jauranol
Maximilian Schwarzmueller
Maximilian Schwarzmueller
Maximilian Schwarzmueller
Bernd Raucher
Maximilian Schwarzmueller
'''
print(savedatalist) #print ['Maximilian Schwarzmueller', 'Maximilian Schwarzmueller', 'Daniel Weat', 'Maximilian Schwarzmueller', 'Mike Jauranol', 'Mike Jauranol', 'Maximilian Schwarzmueller', 'Maximilian Schwarzmueller', 'Maximilian Schwarzmueller', 'Bernd Raucher', 'Maximilian Schwarzmueller']
with open("usernamesnew.json","w") as fileobject:
    json.dump(savedatalist, fileobject)

#How to Convert JSON Data Into a Python Object
import json
class User:
    def __init__(self, guid, isActive, name, email, phone, address):
        self.guid = guid
        self.isActive = isActive
        self.firstname = name["first"]
        self.lastname = name["last"]
        self.email = email
        self.phone = phone
        self.address = address

    @classmethod
    def fromjson(cls, jsonstring):
        jsondictionary = json.loads(jsonstring)
        return cls(**jsondictionary)

    def __repr__(self):
        return f"<User { self.firstname }>"

jsonstring = '''
  {
    "guid": "1f1c4ac7-fc36-4008-935b-d87ffc7d8700",
    "isActive": false,
    "name": {
      "first": "Reid",
      "last": "Warren"
    },
    "email": "reid.warren@undefined.name",
    "phone": "+1 (983) 443-3504",
    "address": "359 Rapelye Street, Holtville, Marshall Islands, 9692"
  }
'''
user = User.fromjson(jsonstring)
print(user) #print <User Reid>
print(user.address) #print <User Reid>
print(user.email) #print reid.warren@undefined.name
print(user.phone) #print +1 (983) 443-3504
userslist = []
with open("bogussamplejsondata.json", "r") as jsonfile:
    userdata = json.loads(jsonfile.read())
    for eachuserdata in userdata:
        userslist.append(User(**eachuserdata))
print(userslist) #print [<User Reid>, <User Amelia>, <User Shari>, <User Lindsay>, <User Mckee>, <User Eunice>, <User Pearlie>, <User Leann>, <User Ashley>, <User Nell>, <User Nita>]

#JSON in Python - Advanced Python 11 - Programming Tutorial
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
converttojson = json.dumps(person)
print(converttojson) #print {"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}  #RM:  false is lowercase
converttojson = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
print(converttojson)
'''
{
    "age"= 30; 
    "city"= "New York"; 
    "hasChildren"= false; 
    "name"= "John"; 
    "titles"= [
        "engineer"; 
        "programmer"
    ]
}
'''
converttojson = json.dumps(person, indent=4, sort_keys=True)
with open("person.json","w") as fileobject:
    json.dump(converttojson, fileobject, indent=4)
convertodictionary = json.loads(converttojson)
print(convertodictionary) #print {'age': 30, 'city': 'New York', 'hasChildren': False, 'name': 'John', 'titles': ['engineer', 'programmer']}
with open("person.json","r") as fileobject:
    persontodictionary = json.load(fileobject)
    print(persontodictionary)
    '''
    {
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
        ]
    }
    '''
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User("Max", 27)
def encodeuser(o):
    if isinstance(o, User):
        return {"name":o.name,"age":o.age,o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSOn serializable")
usertojson = json.dumps(user, default=encodeuser)
print(usertojson) #print {"name": "Max", "age": 27, "User": true}
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name":o.name,"age":o.age,o.__class__.__name__: True}      
        return JSONEncoder.default(self,o)
usertojson = json.dumps(user, cls=UserEncoder)
print(usertojson) #print {"name": "Max", "age": 27, "User": true}
usertojson = UserEncoder().encode(user)
print(usertojson) #print {"name": "Max", "age": 27, "User": true}
usertodictionary = json.loads(usertojson)
print(usertodictionary) #print {'name': 'Max', 'age': 27, 'User': True}
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct
usertodictionary = json.loads(usertojson, object_hook=decode_user)
print(usertodictionary) #print <__main__.User object at 0x7fded4643cc0>
print(type(usertodictionary)) #print <class '__main__.User'>
print(usertodictionary.name) #print Max

#How to Write Python Scripts to Analyze JSON APIs and Sort Results
import json
import time
import requests
import os
r = requests.get("https://formulae.brew.sh/api/formula.json")
packagesjson = r.json()
#print(packagesjson) #print ...c'}}}}, 'keg_only': False, 'bottle_disabled': False, 'options': [], 'build_dependencies': [], 'dependencies': [], 'recommended_dependencies': [], 'optional_dependencies': [], 'uses_from_macos': [], 'requirements': [], 'conflicts_with': [], 'caveats': None, 'installed': [], 'linked_keg': None, 'pinned': False, 'outdated': False}, {'name': 'tokyo-dystopia', 'full_name': 'tokyo-dystopia', 'oldname': None, 'aliases': [], 'versioned_formulae': [], 'desc': 'Lightweight full-text search system', 'homepage': 'https://fallabs.com/tokyodystopia/', 'versions': {'stable': '0.9.15', 'devel': None, 'head': None, 'bottle': True}, 'urls': {'stable': {'url': 'https://fallabs.com/tokyodystopia/tokyodystopia-0.9.15.tar.gz', 'tag': None, 'revision': None}}, 'revision': 0, 'version_scheme': 0, 'bottle': {'stable': {'rebuild': 0, 'cellar': ':any', 'prefix': '/usr/local', 'root_url': 'https://homebrew.bintray.com/bottles', 'files': {'catalina': {'url': 'https://homebrew.bintray.com/bottles/tokyo-dystopia-0.9.15.catalina.bottle.tar.gz', 'sha256': 'eb04133c9d459ee1ab9a4fe00b3f6b31621d9df2672a252784779a44a5991b77'}, 'mojave': {'url': 'https://homebrew.bintray.com/bottles/tokyo-dystopia-0.9.15.mojave.bottle.tar.gz', 'sha256': '056aa0bfed85351c6296b0749dfa15a2e9471ef554796f726708438e312b5790'}, 'high_sierra': {'url': 'https://homebrew.bintray.com/bottles/tokyo-dystopia-0.9.15.high_sierra.bottle.tar.gz', 'sha256': '3f00b619720603bd0712b52d01a355124604637c44cab5a3132fda942f195e2c'}, 'sierra': ...
packagesstring = json.dumps(packagesjson, indent=2) #the s is string
#print(packagesstring)
'''
          "el_capitan": {
            "url": "https://homebrew.bintray.com/bottles/xml-coreutils-0.8.1.el_capitan.bottle.1.tar.gz",
            "sha256": "19bdcacd49657e78f82fd7743a50266ff4945e644b069ac2c39a8787a57911a5"
          },
          "yosemite": {
            "url": "https://homebrew.bintray.com/bottles/xml-coreutils-0.8.1.yosemite.bottle.1.tar.gz",
            "sha256": "1342c807e5ddc23a72e750f07258864fdf2fc1a8ce9072cb7797955fdd0e3656"
          },
'''
#print(packagesstring[0]) #print [
# print(type(packagesstring)) #print <class 'str'>
firstpackagestring = json.dumps(packagesjson[0], indent=2)
# print(type(firstpackagestring)) #print <class 'str'>
# print(firstpackagestring)
'''
{
  "name": "a2ps",
  "full_name": "a2ps",
  "oldname": null,
  "aliases": [],
  "versioned_formulae": [],
  "desc": "Any-to-PostScript filter",
  "homepage": "https://www.gnu.org/software/a2ps/",
  "versions": {
    "stable": "4.14",
    "devel": null,
    "head": null,
    "bottle": true
  },
  "urls": {
    "stable": {
      "url": "https://ftp.gnu.org/gnu/a2ps/a2ps-4.14.tar.gz",
      "tag": null,
      "revision": null
    }
  },
...
'''
#https://formulae.brew.sh/api/formula/a2ps.json  #RM:  the url has the analytics for its software package
firstpackagejsonname = packagesjson[0]  #RM:  also works-->firstpackagejsonname = json.dumps(packagesjson[0], indent=0)
# print(type(firstpackagejsonname)) #print <class 'dict'>
# print(firstpackagejsonname)
'''
{'name': 'a2ps', 'full_name': 'a2ps', 'oldname': None, 'aliases': [], 'versioned_formulae': [], 'desc': 'Any-to-PostScript filter', 'homepage': 'https://www.gnu.org/software/a2ps/', 'versions': {'stable': '4.14', 'devel': None, 'head': None, 'bottle': True}, 'urls': {'stable': {'url': 'https://ftp.gnu.org/gnu/a2ps/a2ps-4.14.tar.gz', 'tag': None, 'revision': None}}, 'revision': 0, 'version_scheme': 0, 'bottle': {'stable': {'rebuild': 3, 'cellar': '/usr/local/Cellar', 'prefix': '/usr/local', 'root_url': 'https://homebrew.bintray.com/bottles', 'files': {'catalina': {'url': 'https://homebrew.bintray.com/bottles/a2ps-4.14.catalina.bottle.3.tar.gz', 'sha256': '98a293e2d83134c9a1c35026f68207d9fc2ac1bde9d7d15dd29849d7d9c5b237'}, 'mojave': {'url': 'https://homebrew.bintray.com/bottles/a2ps-4.14.mojave.bottle.3.tar.gz', 'sha256': 'b3d7d7bd0bfcada7fc2bc2340ab67362e5087e53b4d611d84aafedf713bde6c3'}, 'high_sierra': {'url': 'https://homebrew.bintray.com/bottles/a2ps-4.14.high_sierra.bottle.3.tar.gz', 'sha256': '99646196c8b9e6d5a7b67ecca1589160749d690128bb89aace3b79d4c355dfde'}, 'sierra': {'url': 'https://homebrew.bintray.com/bottles/a2ps-4.14.sierra.bottle.3.tar.gz', 'sha256': '5a1c466a3f833797710464dd1aaf4ad6c9ff0a47de33ab3b2ba9cf0c2be36bfd'}, 'el_capitan': {'url': 'https://homebrew.bintray.com/bottles/a2ps-4.14.el_capitan.bottle.3.tar.gz', 'sha256': '532c3f14debcd59028285dad1d6fe41dbad481718cc1752b1b9e7c05fd82e27f'}}}}, 'keg_only': False, 'bottle_disabled': False, 'options': [], 'build_dependencies': [], 'dependencies': [], 'recommended_dependencies': [], 'optional_dependencies': [], 'uses_from_macos': [], 'requirements': [], 'conflicts_with': [], 'caveats': None, 'installed': [], 'linked_keg': None, 'pinned': False, 'outdated': False}
'''
firstpackagejsonname = packagesjson[0]["name"]
print(firstpackagejsonname) #print a2ps
firstpackagejsondescription = packagesjson[0]["desc"]
packageurl = f"https://formulae.brew.sh/api/formula/{firstpackagejsonname}.json"
r = requests.get(packageurl)
completepackagejson = r.json()
#instructor included the completepackagestring for the watcher to see the a2ps json as a string
completepackagestring = json.dumps(completepackagejson, indent=2)
# print(type(completepackagestring)) #print <class 'str'>
# print(completepackagestring)
'''
{
  "name": "a2ps",
  "full_name": "a2ps",
  "oldname": null,
  "aliases": [],
  "versioned_formulae": [],
  "desc": "Any-to-PostScript filter",
  "homepage": "https://www.gnu.org/software/a2ps/",
  "versions": {
    "stable": "4.14",
    "devel": null,
    "head": null,
    "bottle": true
  },
  "urls": {
    "stable": {
      "url": "https://ftp.gnu.org/gnu/a2ps/a2ps-4.14.tar.gz",
      "tag": null,
      "revision": null
    }
  },
...
'''
#firstpackagestringanalytics = packagesjson[0]["analytics"]["install_on_request"]  #RM:  error message I don't know why?
firstpackagestringanalytics = completepackagejson["analytics"]["install_on_request"]
print(firstpackagestringanalytics) #print {'30d': {'a2ps': 81}, '90d': {'a2ps': 247}, '365d': {'a2ps': 1133}}
firstpackagestringanalytics30d = completepackagejson["analytics"]["install_on_request"]["30d"][firstpackagejsonname]
print(firstpackagestringanalytics30d) #print 81
firstpackagestringanalytics90d = completepackagejson["analytics"]["install_on_request"]["90d"][firstpackagejsonname]
firstpackagestringanalytics365d = completepackagejson["analytics"]["install_on_request"]["365d"][firstpackagejsonname]
print(firstpackagejsonname, firstpackagejsondescription, firstpackagestringanalytics30d, firstpackagestringanalytics90d, firstpackagestringanalytics365d) #print a2ps Any-to-PostScript filter 81 247 1133
r = requests.get("https://formulae.brew.sh/api/formula.json")
packagesjson = r.json()
print(len(packagesjson)) #print 5072
#instructor adds a sleep to slow down API requesting 5,072 packages
packageanalyticslist = []
timerstart = time.perf_counter()
counterlimitpackagesjson = 1
for eachpackagesjson in packagesjson:    
    jsonname = eachpackagesjson["name"]
    jsondescription = eachpackagesjson["desc"]
    packageurl = f"https://formulae.brew.sh/api/formula/{jsonname}.json"
    r = requests.get(packageurl)
    completepackagejson = r.json()
    packageanalytics30d = completepackagejson["analytics"]["install_on_request"]["30d"][jsonname]
    packageanalytics90d = completepackagejson["analytics"]["install_on_request"]["90d"][jsonname]
    packageanalytics365d = completepackagejson["analytics"]["install_on_request"]["365d"][jsonname]
    datadictionary = {"name":jsonname,"description":jsondescription,"analytics":{"30d":packageanalytics30d,"90d":packageanalytics90d,"365d":packageanalytics365d}}
    packageanalyticslist.append(datadictionary)
    print(f"Got {jsonname} in {r.elapsed.total_seconds()} seconds")
    time.sleep(r.elapsed.total_seconds())    
    #break #instructor added break statement to test for first result only.
    #RM:  get 50 packages instead of all the packages.
    if counterlimitpackagesjson == 50:
        break
    else:
        counterlimitpackagesjson+=1
print(packageanalyticslist)
timerend = time.perf_counter()
print(f"Finished in {timerend-timerstart} seconds")
os.remove("packagesinfo.json")
with open("packagesinfo.json","w") as fileobject:
    json.dump(packageanalyticslist, fileobject, indent=2) #json.dumps with an s means string

#twitterinformation.py
import tweepy
import twitter_credentials as tc
#Create an api object.  Establish a connection with my developer information.  api object talk to twitter, read data to Twitter, write data to Twitter.  Store information in variable api.
authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)
#Save my user's information.  Download using tweepy ._json as json file.
twitteruser = "inin61"
userinformation = api.get_user(twitteruser)
print(userinformation) #print User(_api=<tweepy.api.API object at 0x7f3a919482b0>, _json={'id': 86863717, 'id_str': '86863717', 'name': 'Raymond Mar', 'screen_name': 'inin61', 'location': 'San Jose, CA', 'profile_location': None, 'description': "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", 'url': 'https://t.co/jXjuhIMFeG', 'entities': {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 66, 'friends_count': 49, 'listed_count': 9, 'created_at': 'Mon Nov 02 03:27:17 +0000 2009', 'favourites_count': 501, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 6486, 'lang': None, 'status': {'created_at': 'Mon Jul 06 16:24:47 +0000 2020', 'id': 1280175872297795584, 'id_str': '1280175872297795584', 'text': 'Which is the smarter dog?  Snoopy from Peanuts or Brain from Inspector Gadget.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="http://www.tweetcaster.com" rel="nofollow">TweetCaster for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/86863717/1489186606', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none', 'suspended': False, 'needs_phone_verification': False}, id=86863717, id_str='86863717', name='Raymond Mar', screen_name='inin61', location='San Jose, CA', profile_location=None, description="Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", url='https://t.co/jXjuhIMFeG', entities={'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=66, friends_count=49, listed_count=9, created_at=datetime.datetime(2009, 11, 2, 3, 27, 17), favourites_count=501, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=6486, lang=None, status=Status(_api=<tweepy.api.API object at 0x7f3a919482b0>, _json={'created_at': 'Mon Jul 06 16:24:47 +0000 2020', 'id': 1280175872297795584, 'id_str': '1280175872297795584', 'text': 'Which is the smarter dog?  Snoopy from Peanuts or Brain from Inspector Gadget.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="http://www.tweetcaster.com" rel="nofollow">TweetCaster for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 7, 6, 16, 24, 47), id=1280175872297795584, id_str='1280175872297795584', text='Which is the smarter dog?  Snoopy from Peanuts or Brain from Inspector Gadget.', truncated=False, entities={'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, source='TweetCaster for Android', source_url='http://www.tweetcaster.com', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, lang='en'), contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/86863717/1489186606', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none', suspended=False, needs_phone_verification=False)
print(type(userinformation)) #print <class 'tweepy.models.User'>
print(userinformation._json) #print {'id': 86863717, 'id_str': '86863717', 'name': 'Raymond Mar', 'screen_name': 'inin61', 'location': 'San Jose, CA', 'profile_location': None, 'description': "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", 'url': 'https://t.co/jXjuhIMFeG', 'entities': {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 66, 'friends_count': 49, 'listed_count': 9, 'created_at': 'Mon Nov 02 03:27:17 +0000 2009', 'favourites_count': 501, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 6486, 'lang': None, 'status': {'created_at': 'Mon Jul 06 16:24:47 +0000 2020', 'id': 1280175872297795584, 'id_str': '1280175872297795584', 'text': 'Which is the smarter dog?  Snoopy from Peanuts or Brain from Inspector Gadget.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="http://www.tweetcaster.com" rel="nofollow">TweetCaster for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/86863717/1489186606', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none', 'suspended': False, 'needs_phone_verification': False}
print(type(userinformation._json)) #print <class 'dict'>
jsonuserinformation = userinformation._json
with open("inin61.json","w") as fileobject:
	json.dump(jsonuserinformation, fileobject)
#Load with my user's information.  Extract my id and my webpage.
with open("inin61.json","r") as fileobject:
	inin61 = json.load(fileobject)
print(inin61)
print(type(inin61)) #print <class 'dict'>
print(inin61["id"]) #print 86863717
print(inin61["entities"]) #print {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}
print(type(inin61["entities"])) #print <class 'dict'>
print(inin61["entities"]["url"]["urls"]) #print [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]
print(type(inin61["entities"]["url"]["urls"])) #print <class 'list'>
print(inin61["entities"]["url"]["urls"][0]) #print {'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}
print(type(inin61["entities"]["url"]["urls"][0])) #print <class 'dict'>
print(inin61["entities"]["url"]["urls"][0]["expanded_url"]) #print https://www.innovateinfinitely.com

#Use For loop to see all json fields
for eachtweeturl in status._json["quoted_status"]["entities"]:
	print(eachtweeturl)
	'''
	hashtags
	symbols
	user_mentions
	urls
	'''
#Use For loop to see all json fields complete
import tweepy
import twitter_credentials as tc
authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=1):
	for eachtweeturl in status._json:
		print(eachtweeturl)
		'''
		created_at
		id
		id_str
		full_text
		truncated
		display_text_range
		entities
		source
		in_reply_to_status_id
		in_reply_to_status_id_str
		in_reply_to_user_id
		in_reply_to_user_id_str
		in_reply_to_screen_name
		user
		geo
		coordinates
		place
		contributors
		retweeted_status
		is_quote_status
		retweet_count
		favorite_count
		favorited
		retweeted
		lang
		'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=1):
	for allreretweeted_status in status._json["retweeted_status"]:
		print(allreretweeted_status)
		'''
		created_at
		id
		id_str
		full_text
		truncated
		display_text_range
		entities
		extended_entities
		source
		in_reply_to_status_id
		in_reply_to_status_id_str
		in_reply_to_user_id
		in_reply_to_user_id_str
		in_reply_to_screen_name
		user
		geo
		coordinates
		place
		contributors
		is_quote_status
		retweet_count
		favorite_count
		favorited
		retweeted
		possibly_sensitive
		lang
		'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]:
			print(eachtweeturl)
			'''
			created_at
			id
			id_str
			full_text
			truncated
			display_text_range
			entities
			extended_entities
			source
			in_reply_to_status_id
			in_reply_to_status_id_str
			in_reply_to_user_id
			in_reply_to_user_id_str
			in_reply_to_screen_name
			user
			geo
			coordinates
			place
			contributors
			is_quote_status
			retweet_count
			favorite_count
			favorited
			retweeted
			possibly_sensitive
			lang
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["entities"]:
			print(eachtweeturl)
			'''
			hashtags
			symbols
			user_mentions
			urls
			media
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["entities"]["media"]:
			print(eachtweeturl)
			'''
			{'id': 1298761835177562114, 'id_str': '1298761835177562114', 'indices': [244, 267], 'media_url': 'http://pbs.twimg.com/amplify_video_thumb/1298761835177562114/img/D22KhvlXVGQUfIoc.jpg', 'media_url_https': 'https://pbs.twimg.com/amplify_video_thumb/1298761835177562114/img/D22KhvlXVGQUfIoc.jpg', 'url': 'https://t.co/HRoLbCS4SN', 'display_url': 'pic.twitter.com/HRoLbCS4SN', 'expanded_url': 'https://twitter.com/espn/status/1298761885823774721/video/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 1200, 'h': 675, 'resize': 'fit'}, 'small': {'w': 680, 'h': 383, 'resize': 'fit'}, 'large': {'w': 1280, 'h': 720, 'resize': 'fit'}}}
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"]:
			print(eachtweeturl)
			'''
			{'id': 1298761835177562114, 'id_str': '1298761835177562114', 'indices': [244, 267], 'media_url': 'http://pbs.twimg.com/amplify_video_thumb/1298761835177562114/img/D22KhvlXVGQUfIoc.jpg', 'media_url_https': 'https://pbs.twimg.com/amplify_video_thumb/1298761835177562114/img/D22KhvlXVGQUfIoc.jpg', 'url': 'https://t.co/HRoLbCS4SN', 'display_url': 'pic.twitter.com/HRoLbCS4SN', 'expanded_url': 'https://twitter.com/espn/status/1298761885823774721/video/1', 'type': 'video', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 1200, 'h': 675, 'resize': 'fit'}, 'small': {'w': 680, 'h': 383, 'resize': 'fit'}, 'large': {'w': 1280, 'h': 720, 'resize': 'fit'}}, 'video_info': {'aspect_ratio': [16, 9], 'duration_millis': 118919, 'variants': [{'content_type': 'application/x-mpegURL', 'url': 'https://video.twimg.com/amplify_video/1298761835177562114/pl/4vy7og0R6lw6Ubi4.m3u8?tag=13'}, {'bitrate': 288000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1298761835177562114/vid/480x270/3rEQFbXpOPrvg0Dr.mp4?tag=13'}, {'bitrate': 832000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1298761835177562114/vid/640x360/RNm9PsDXaXfGBMPi.mp4?tag=13'}, {'bitrate': 2176000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1298761835177562114/vid/1280x720/tdEUPgemWBdCCSA8.mp4?tag=13'}]}, 'additional_media_info': {'title': '', 'description': '', 'monetizable': False}}
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]:
			print(eachtweeturl)
			'''
			id
			id_str
			indices
			media_url
			media_url_https
			url
			display_url
			expanded_url
			type
			sizes
			video_info
			additional_media_info
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["sizes"]:
			print(eachtweeturl)
			'''
			thumb
			medium
			small
			large
			'''
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=4):
	if status._json["id"] == 1298789501565693952:
		for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]:
			print(eachtweeturl)
			'''
			aspect_ratio
			duration_millis
			variants
			'''

#Python Crash Course ch16downloadingdata.py
import json

filename = "population_data.json"
with open(filename, "r") as fileobject:
    loadpopulationdata = json.load(fileobject)
#print(loadpopulationdata) #print [{'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1960', 'Value': '96388069'}, {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1961', 'Value': '98882541.4'}, {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1962', 'Value': '101474075.8'}, {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1963', 'Value': '104169209.2'}, . . .
for eachloadpopulationdata in loadpopulationdata:
    #print(eachloadpopulationdata) #print 'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1960', 'Value': '96388069'}\n {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1961', 'Value': '98882541.4'}\n {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1962', 'Value': '101474075.8'}\n {'Country Name': 'Arab World', 'Country Code': 'ARB', 'Year': '1963', 'Value': '104169209.2'}\n . . .
    #print(eachloadpopulationdata["Year"]) #print 1960\n 1961\n 1962\n 1963
    if eachloadpopulationdata["Year"] == "2010":
        countryname = eachloadpopulationdata["Country Name"]
        population = eachloadpopulationdata["Value"]
        #print(countryname + ", " + population) #print Arab World, 357868000\n Caribbean small states, 6880000\n East Asia & Pacific (all income levels), 2201536674\n . . .
        populationasinteger = int(float(eachloadpopulationdata["Value"]))
        print(populationasinteger) #print 357868000 6880000 2201536674
        print(type(populationasinteger)) #print <class 'int'> <class 'int'> <class 'int'>