"""
You are tasked with a creating python programme to manage a companies employee records stored in csv files the programme should read the employee details 
from the csv file,filter the records based on a condition and write the filters record to a new csv file 
    - input file = employee.csv - contain the folowing field - employeeID,name,department,salary
    - output file -  high_salary_employees.csv - you will create this file it should contain record of employees whose salaries are above 57,000 the field should remain the same
Task - read the input file use csv.Reader to read employees.csv and display all the records on the console
     - filter the record identify employees with the salary>57000
     - write the filtered records use csv.DictWriter to write the filtered records to a new file name High salary employess.csv

"""

import csv

# Input and Output file paths
input_file = 'employee.csv'  # Input CSV file
output_file = 'high_salary_employees.csv'  # Output CSV file

# Step 1: Read and Display All Records
print("All Employee Records:")
with open(input_file, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)  # Using csv.reader to read rows as lists
    for row in csv_reader:
        print(row)

# Step 2: Filter Employees with Salary > 57,000
high_salary_employees = []  # List to store filtered employees

with open(input_file, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # Using DictReader to read rows as dictionaries
    for row in csv_reader:
        # Check if the salary is greater than 57,000
        if int(row["Salary"]) > 57000:
            high_salary_employees.append(row)

# Step 3: Write Filtered Records to a New CSV File
if high_salary_employees:
    with open(output_file, 'w', newline='') as csv_file:
        # Ensure these field names match exactly with the input file column headers
        field_names = ["EmployeeID", "Name", "Department", "Salary"]  
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
        # Write header and filtered data
        csv_writer.writeheader()
        csv_writer.writerows(high_salary_employees)

    print(f"Filtered records have been written to '{output_file}'.")
else:
    print("No employees found with a salary greater than 57,000.")





