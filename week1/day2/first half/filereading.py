#f = open('names.txt',"x")

import csv

import json

with open('names.txt',"w") as wr:
    wr.write(
        "arunn \n priya \n rahul \n karthik \n divya"
    )


with open('names.txt') as r:
    print(r.read())




#CSV Reading and Writing

students = [
    {"name": "Alice", "marks": 75},
    {"name": "Bob", "marks": 55},
    {"name": "Charlie", "marks": 82},
    {"name": "David", "marks": 60},
    {"name": "Emma", "marks": 91}
]

filtered_students = [
    student for student in students
    if student["marks"] > 60
]


# field Names [names,marks]

f=["name","marks"]

#name of the csv file

fn ="students_marks_record.csv"


#writing csv file 

with open(fn,"w",newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames= f)

     # Writing headers (field names)
    writer.writeheader()
    writer.writerows(filtered_students)



with open("students.json","w") as file:
    json.dump(students,file,indent=2)
 


with open("students.json","r") as file:
    load_students = json.load(file)
    for student in load_students:
        print(student)




try:
    with open("sample.txt",'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("Error:",e)