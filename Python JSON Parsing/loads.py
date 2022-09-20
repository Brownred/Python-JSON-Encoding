# parse a JSON string format

import json

developerJsonString = '''{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "web development"
    ],
    "email": "Janedoe@pynative.com",
    "projects": [
        "python Data Mining",
        "Python Data Science"
    ]
}
'''

developerDict = json.loads(developerJsonString)

print(developerDict["name"])
print(developerDict["salary"])
print(developerDict["skills"])
print(developerDict["email"])
print(developerDict["projects"])