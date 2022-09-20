import json

# parse_float and parse_int will be called with the string of every JSON float and integer

"""
Suppose the JSON document cantains many float values, and you want to round all float
values to two-decimal point. 
- In this case, define a custom function that perfoms whatever rounding you desire
and pass that function to parse_float kwwarg.

To perform any operations on integer values write a custom function and pass it to 
parse_int kwarg
"""

def roundFloats(salary):
    return round(float(salary), 2)

def salaryToDeduct(leaveDays):
    salaryPerDay = 465
    return int(leaveDays) * salaryPerDay

with open(r"C:\Users\ACE\Desktop\Dealing with JSON data\Python JSON Parsing\developerJsonString.json","r") as json_file:
    developer = json.load(json_file, parse_float = roundFloats, parse_int = salaryToDeduct)
    
    #after parse float
    print("salary:", developer["salary"])
    
    #after parse_int
    print("Salary to deduct:", developer["leaveDays"])
    