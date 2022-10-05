# inheriting from dict to make class JSON serializable

"""
This works if your class is not complicated. For trickier things you will have to set keys explicitly
If you want to use json.dumps() as is, then a simple solution is inheriting from dict.

"""
import json

class Employee(dict):
    def __init__(self, name, age, salary, address):
        dict.__init__(self, name=name, age=age, salary=salary, address=address )
    
class Address(dict):
    def __init__(self, city, street, pin):
        dict.__init__(self, city=city, street=street, pin=pin)

address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("Jhon", 32, 9000, address)

print("Encode into JSON formatted Data")
employeeJSON = json.dumps(employee, indent=2)
print(employeeJSON)

#load it to check if we can decode it or not.
employeeJSONData = json.loads(employeeJSON)
print(employeeJSONData)