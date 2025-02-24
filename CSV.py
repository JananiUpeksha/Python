import csv
#Read as list
csv_path = 'customers-100.csv'
with open(csv_path,'r',newline='') as csv_file:
    for row in csv_file:
        print(row,type(row))



csv_file_path = 'customers-10.csv'
data = [
    {"name": "Janani", "age": 24, "city": "Kadawatha"},
    {"name": "Senumi", "age": 23, "city": "Panadura"},
    {"name": "Thisanga", "age": 19, "city": "Panadura"},
    {"name": "Dimagi", "age": 21, "city": "Panadura"} 
]
field_names = ["name", "age", "city"]

# Open the CSV for writing
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=field_names)
    
    # Write the header
    csv_writer.writeheader()
    
    # Write the data rows to the CSV file
    for row in data:
        csv_writer.writerow(row)

#Reading as a dict
with open(csv_file_path, 'r') as file:
    rows = csv.DictReader(file)
    for row in rows:
        print(row,type(row))

