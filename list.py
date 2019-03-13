import json

# a Python object (dict):
x = {
  "name": "Carlos",
  "age": 22,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

