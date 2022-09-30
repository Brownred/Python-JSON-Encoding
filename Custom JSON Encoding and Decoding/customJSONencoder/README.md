# serializing arbitrary python objects to JSON

Convert any custom python object to JSON formatted data.
The built-in JSON module only handle python primitive types that have direct JSON equivalent (e.g. dictionary, lists, strings, numbers, None, etc).
JSON Encoder json.dump() and json.dummps() only knows how to serialize the basic set of object types by default
To solve this build a custom encoder to make our class JSON serializable.

## Goals

    .Write your own *custom JSON Encoder* to make class JSON serializable.
    .Create custom  toJSON() method to make python class JSON serializable
    . Use *jsonpickle* module to make class JSON serializable
    .How to inherit class form dict to make class JSON serializable
