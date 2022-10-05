# Implementing a custom JSON decoder using json.load()
# Writing a custom JSON decoder and pass it to the json.loads() method so as to get a custom Class instead of a dictionary.
# use the _object_hook_ parameter of the load method

import json
from collections import namedtuple
from json import JSONEncoder

def movieJSONDecode(movieDict):
    return namedtuple(Movie, movieDict.keys())(*movieDict.values())
#class for your refernce
class Movie:
    def __init__(self, name="", year=0, income=0):
        self.name = name
        self.year = year
        self.income = income

#suppose you have this json document
movieJson = """{
    "name": "Interstellar",
    "year": 2014,
    "Income": 7000000    
}"""

#parse JSON into a movie object
movieObj = json.loads(movieJson, object_hook = movieJSONDecode)

print(movieObj.income)

