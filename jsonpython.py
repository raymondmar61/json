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