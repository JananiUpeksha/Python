import json
json_file = 'example_1.json'
with open(json_file, 'r') as file:
    data = json.load(file)
print(data, type(data))


data = {
    "name": "Janani Upeksha",
    "age": 24,
    "city": "Kadawatha" 
}

json_file_path = 'example_3.json'
with open(json_file_path, 'w') as file:
    json_data = json.dumps(data, indent=4)  # Convert data to JSON format with indentation dump - return a string, indent - create a structure like a dict
    file.write(json_data)  # Write the formatted JSON data to the file

"""
