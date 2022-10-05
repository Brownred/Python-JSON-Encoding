# Method 1:

# writing a custom JSONEncoder to make class JSON serializable
"""python json module has a JSONEncoder class, which you can extend if you want more customization i.e you will have to
subclass JSONEncoder so you can implement your custom JSON serialization

The json.dump() and json.dumps() method of the json module has a cls kwarg which you can pass a customJSON Encoder, which
tells dump() or dumps() method how to encode your object into json formatted data

Your custom JSON Encoder subclass will overide the default() method to serialize additional types. Specify it with the cls
kwarg in json.dumps() method; otherwise default JSONEncoder is used. Example: json.dumps(cls = CustomerEncoder)
"""
import json
from json import JSONEncoder

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin
        
# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    
address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 7000, address)                

#print("Printing to check how it will look like")
#print(EmployeeEncoder().encode(employee))

print("Encode Employee object into JSON formatted data using custom jsonencoder")
employeeJSONData = json.dumps(employee, indent=4, cls=EmployeeEncoder)
print(employeeJSONData)

#Let's load it using the load method to check if we can decode it or not.
print("Decode JSON formatted data")
employeeJSON = json.loads(employeeJSONData)
print(employeeJSON)
