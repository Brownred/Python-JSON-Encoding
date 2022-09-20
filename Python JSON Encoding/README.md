# Serialization; Python JSON Encoding

Using The _requests_ module in python, I accessed github public timeline using the _.get_ method and got back a response.
Since I was dealing with JSON data, decode it using the builtin JSON decoder in the requests module. 

The result after decoding is a list of dictionaries.

Using the json module I encoded the python object into json format in a file using _json.dumps_

## Compact Encoding

Perfomed compact encoding to save file space by changing JSON key-value separator.
Using the _separator_ argument of a json.dump() method sepecifying a separator between key and value (Removing extra spacing between JSON key-value). 
(Separators = (",",":")) To remove the white spaces from JSON to make the JSON more compact