# To read JSON data from a file and convert it into a dictionary
# Using the test.json folder

import json

with open ("test.json","r") as json_file:
    # Converted json encoded data into python dictionary
    read_file = json.load(json_file)
    
    # Print key value pair since file is already converted to python object
    for key, value in read_file.items():
        print(key, ":", value)
    

