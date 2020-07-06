import json

def installsort(package):
	return package["analytics"]["30d"]

with open("packagesinfo.json","r") as fileobject:
	data = json.load(fileobject)
#print(data)
'''
[{'name': 'a2ps', 'description': 'Any-to-PostScript filter', 'analytics': {'30d': 76, '90d': 244, '365d': 1131}}, {'name': 'a52dec', 'description': "Library for decoding ATSC A/52 streams (AKA 'AC-3')", 'analytics': {'30d': 29, '90d': 98, '365d': 360}}, {'name': 'aacgain', 'description': 'AAC-supporting version of mp3gain', 'analytics': {'30d': 54, '90d': 172, '365d': 595}}, {'name': 'aalib', 'description': 'Portable ASCII art graphics library', 'analytics': {'30d': 48, '90d': 187, '365d': 849}}, {'name': 'aamath', 'description': 'Renders mathematical expressions as ASCII art', 'analytics': {'30d': 13, '90d': 50, '365d': 217}}, {'name': 'aardvark_shell_utils', 'description': 'Utilities to aid shell scripts or command-line users', 'analytics': {'30d': 4, '90d': 29, '365d': 125}}, {'name': 'abcde', 'description': 'Better CD Encoder', 'analytics': {'30d': 29, '90d': 107, '365d': 574}}, {'name': 'abcl', 'description': 'Armed Bear Common Lisp: a full implementation of Common Lisp', 'analytics': {'30d': 68, '90d': 159, '365d': 340}}, {'name': 'abcm2ps', 'description': 'ABC music notation software', 'analytics': {'30d': 50, '90d': 97, '365d': 432}}, {'name': 'abcmidi', 'description': 'Converts abc music notation files to MIDI files', 'analytics': {'30d': 149, '90d': 307, '365d': 902}}, {'name': 'abduco', 'description': 'Provides session management: i.e. separate programs from terminals', 'analytics': {'30d': 13, '90d': 34, '365d': 149}}, {'name': 'abnfgen', 'description': 'Quickly generate random documents that match an ABFN grammar', 'analytics': {'30d': 3, '90d': 8, '365d': 48}}, {'name': 'abook', 'description': 'Address book with mutt support', 'analytics': {'30d': 40, '90d': 227, '365d': 489}}, {'name': 'abseil', 'description': 'C++ Common Libraries', 'analytics': {'30d': 43, '90d': 127, '365d': 172}}, {'name': 'abuse', 'description': 'Dark 2D side-scrolling platform game', 'analytics': {'30d': 44, '90d': 93, '365d': 393}}, {'name': 'abyss', 'description': 'Genome sequence assembler for short reads', 'analytics': {'30d': 28, '90d': 92, '365d': 562}}, {'name': 'ace', 'description': 'ADAPTIVE Communication Environment: OO network programming in C++', 'analytics': {'30d': 77, '90d': 197, '365d': 805}}, ...]
'''
print(type(data)) #print <class 'list'>
print(data[0]) #print {'name': 'a2ps', 'description': 'Any-to-PostScript filter', 'analytics': {'30d': 76, '90d': 244, '365d': 1131}}
print(type(data[0])) #print <class 'dict'>
print(data[0]["name"]) #print a2ps
print(data[0]["analytics"]) #print {'30d': 76, '90d': 244, '365d': 1131}
print(data[0]["analytics"]["90d"]) #print 244
data.sort(key=installsort, reverse=True)
datastring = json.dumps(data, indent=2)
print(datastring)
'''
[
  {
    "name": "ack",
    "description": "Search tool like grep, but optimized for programmers",
    "analytics": {
      "30d": 7802,
      "90d": 18366,
      "365d": 101982
    }
  },
  {
    "name": "adns",
    "description": "C/C++ resolver library and DNS resolver utilities",
    "analytics": {
      "30d": 1668,
      "90d": 2047,
      "365d": 4338
    }
  },
  {
    "name": "adwaita-icon-theme",
    "description": "Icons for the GNOME project",
    "analytics": {
      "30d": 920,
      "90d": 4340,
      "365d": 14304
    }
  },
...
'''
data.sort(key=installsort, reverse=True)
topfive = json.dumps(data[:5], indent=2)
print(topfive)
'''
[
  {
    "name": "ack",
    "description": "Search tool like grep, but optimized for programmers",
    "analytics": {
      "30d": 7802,
      "90d": 18366,
      "365d": 101982
    }
  },
  {
    "name": "adns",
    "description": "C/C++ resolver library and DNS resolver utilities",
    "analytics": {
      "30d": 1668,
      "90d": 2047,
      "365d": 4338
    }
  },
  {
    "name": "adwaita-icon-theme",
    "description": "Icons for the GNOME project",
    "analytics": {
      "30d": 920,
      "90d": 4340,
      "365d": 14304
    }
  },
  {
    "name": "activemq",
    "description": "Apache ActiveMQ: powerful open source messaging server",
    "analytics": {
      "30d": 854,
      "90d": 2584,
      "365d": 10719
    }
  },
  {
    "name": "acme",
    "description": "Crossassembler for multiple environments",
    "analytics": {
      "30d": 789,
      "90d": 1791,
      "365d": 11201
    }
  }
]
'''
extractvideodata = [item for item in data if "video" in item["description"]]
print(extractvideodata) #print [{'name': 'advancemame', 'description': 'MAME with advanced video support', 'analytics': {'30d': 16, '90d': 52, '365d': 212}}]
data.sort(key=installsort, reverse=True)
datastring = json.dumps(extractvideodata, indent=2)
print(datastring)
'''
[
  {
    "name": "advancemame",
    "description": "MAME with advanced video support",
    "analytics": {
      "30d": 16,
      "90d": 52,
      "365d": 212
    }
  }
]
'''
