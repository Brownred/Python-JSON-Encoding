# Using toJSON() Method to make class JSON serializable

"""
This is a simple and straight forward solution.
Instead of making class JSON serializable, we can implement a serializer method in the class.
So we dont need to write custom JSONEncoder.
This toJSON() serializer will return the JSON representation of the object. i.e. it will convert python objects to JSON
string  
"""
# Example:

import json

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address
        
    def tojson(self):
        return json.dumps(self, default = lambda o: o.__dict__)
    
class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 7000, address)

print("Encode into JSON formatted Data")
employeeJSONData = json.dumps(employee.tojson(), indent = 4)
print(employeeJSONData)            

"""We are able to encode and decode Employee object into JSON formatted stream.
We use default dumps() method to serialize additional types to dict and converted to newly created dict to json string
"""
# Refer to decode JSON into custom Python object instead of a dictionary if you want to decode JSON back to the Custom Python object

