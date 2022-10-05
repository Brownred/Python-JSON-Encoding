# Using the jsonpickle module to make class JSON serializable

"""
Json pickle is a python library designed to work with complex python object
It is used for serialization of complex python objects into JSON and also desirialization from JSON to complex
python objects

Execute jsonpickle.encode(object) to serialize custom Python Object
"""

import json
import jsonpickle
from json import JSONEncoder

class Employee(object):
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address
        
class Address(object):
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin
    
address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("Jhon", 9000, address)

print("Encode Object into JSON formatted data using jsonpickle")
empJSON = jsonpickle.encode(employee, unpicklable=True, indent=4)
# unpickable=True coz of decoding this data back to Employee object
"""If you will never need to load (regenerate the python class from JSON), you can pass
in the keyword unpickable=False to prevent extra information form being added to JSON.
"""

print(empJSON)

print("Decode JSON formatted data using jsonpickle")
EmployeeJSON = jsonpickle.decode(empJSON)
print(EmployeeJSON)    
    

