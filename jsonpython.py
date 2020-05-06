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