import json
"""
json
"""

stringOfJsonData = '{"name": "yinlei", "sex": "male", "age": 23}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

pythonValue = {'name': 'yinlei', 'sex': 'male', 'age': 23}
strOfJsonData = json.dumps(pythonValue)
print(strOfJsonData)