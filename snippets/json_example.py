import json

json_data = '''
{
    "name": "Alice",
    "age": 30,
    "is_student": false
}
'''

data = json.loads(json_data)

print("Name:", data['name'])  # Output: Name: Alice
print("Age:", data['age'])  # Output: Age: 30
print("Is Student:", data['is_student'])  # Output: Is Student: False

python_data = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "courses": ["Art", "History"]
}

json_string = json.dumps(python_data, indent=4)
print(json_string)