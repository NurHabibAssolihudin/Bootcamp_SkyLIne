#  PYTHON JSON
# Import
import json

# json file
json_file = '{"name":"NurHabib","age":17,"city":"Ciamis"}'

# Parese Ke Dictionary
data_json = json.loads(json_file)
print(data_json["age"])

# Parse Ke JSON
json_data = json.dumps(data_json)
print(json_data)

# Format
json_data = json.dumps(data_json, indent=4, sort_keys=True)
print(json_data)