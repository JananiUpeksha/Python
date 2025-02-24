"""You are given a file name student.json which contains info about students and there grades your task is to 
    - read the json file
    - display the name of all students who scored above 75 
    - add the new student record to the file 
    - save the updated data back to the json file"""

import json

# Initial data
data = [
    {"name": "Janani", "grade": 65},
    {"name": "Senumi", "grade": 95},
    {"name": "Thisanga", "grade": 75},
    {"name": "Dimagi", "grade": 85}
]

json_file_path = 'exampleSTUDENT.json'

# Write initial data to the file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

# Read the data back from the file
with open(json_file_path, 'r') as file:
    data_read = json.load(file)

    # Print names of students with grades above 75
    for student in data_read:
        if student["grade"] > 75:
            print("Name:", student["name"])

# Get user input for a new student
name = input("Enter the name: ")
grade = int(input("Enter the grade: "))  # Ensure the grade is an integer
new_entity = {"name": name, "grade": grade}  # Create a dictionary

# Append the new student data to the list
data_read.append(new_entity)

# Write the updated data back to the file
with open(json_file_path, 'w') as file:
    json.dump(data_read, file, indent=4)

# Read the final data from the file and print it
with open(json_file_path, 'r') as file:
    final_data = json.load(file)
    print("\nFinal JSON content after adding new student:")
    print(json.dumps(final_data, indent=4))  # Pretty print the final JSON content

print("New student added successfully.")
