# Serialization; Python JSON Encoding

Using The _requests_ module in python, I accessed github public timeline using the _.get_ method and got back a response.
Since I was dealing with JSON data, decode it using the builtin JSON decoder in the requests module. 

The result after decoding is a list of dictionaries.

Using the json module I encoded the python object into json format in a file using _json.dumps_
