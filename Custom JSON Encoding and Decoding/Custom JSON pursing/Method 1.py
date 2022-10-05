# Using namedtuple and object_hook to convert JSON data into a Custom Python Object

import json 
from collections import namedtuple
from json import JSONEncoder

def customStudentDecoder(studentDict):
    return namedtuple("X", studentDict.keys())(*studentDict.values())

class Student:
    def __init__(self,rollnumber,Name):
        self.rollnumber = rollnumber
        self.Name = Name

# Json response
studentJsonData = '{"rollnumber": 1, "Name": "Emma"}'

# Parse JSON into an object with attributes corresponding dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print(student)
