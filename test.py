import requests
import json

# From github public timeline
response = requests.get('https://api.github.com/events')
# since I was dealing with Json data, decode it using the builtin JSON decoder
# response.json() 
# >>> #The result is a list of dictionaries

# Check the len of the list of decoded response
print(len(response.json()))

# Using the json module encode the python object into json format in a file
with open (r"C:\Users\ACE\Desktop\test.json", "w") as json_file:
    # pick a random position of a dictionary in the list
    # Perform compact encoding
    json.dump(response.json()[10], json_file, indent = 4, separators=(",",":"))
    
# Done writing pretty printed JSON data into a file (test.json)
