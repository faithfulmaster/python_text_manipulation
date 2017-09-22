import json
import csv

# oen json file for readinf=d
infile = open("input.json", "r")
employee_parsed = json.loads(infile.read())
emp_data = employee_parsed['Employee']

# open csv file for writing
employ_data = open('EmployData.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(employ_data)

# Writing to csv file
count = 0
for emp in emp_data:
      if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(emp.values())

# close the csv file
employ_data.close()
