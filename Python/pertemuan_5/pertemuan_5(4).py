# PRAKTEK
import json

# Open & Read
json_file = open("pertemuan_5.json")
file_json = json_file.read()

# Loads File
file_json = json.loads(file_json)
print(file_json)

json_file.close()

json_file = open("pertemuan_5.json")
file = json_file.read()
file = json.loads(file)
file = list(file)
file.append({
    "name" : "Aji",
    "age" : 17,
    "city" : "Kawali"
})
file = json.dumps(file)
json_file.close()

json_file = open("pertemuan_5.json", "w")
json_file.write(file)
json_file.close()

json_file = open("pertemuan_5.json")
print(json_file.read())

