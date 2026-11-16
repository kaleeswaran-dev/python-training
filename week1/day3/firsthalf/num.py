import numpy as np

import pandas as pd


marks = np.array([[70, 80, 90],
[60, 75, 85],
[88, 92, 79],
[55, 65, 70]])

print(marks)

print(f'marks { marks.shape}')

multi = np.array([
    [
        [60, 75, 85],
        [88, 92, 79]
    ],
    [
        [60, 75, 85],
        [88, 92, 79]
    ],
]
)

"""
slicing of first two students and last subjects
"""
print(f'print 2 students they are last subject{marks[0:2,2]}')


print(f'to find axis=1 is average{marks.mean(axis=1)}') #===> calculate row wise move on column wise 

print(f'to find axis=0 is average{marks.mean(axis=0)}') #===> calculate colum wise move on row wise 
# dtype ===> dtype use to stored value is size

#if we need to stored value size dtype = np.int8 ===> like np.which data type we stored and they are value

#ndim ===> we need to dimensions


# we need to access 3D array we need to deal layers,row,column


print(type(marks))


print(marks.dtype)


print(marks.ndim)

print(multi.ndim)


"""
how we achive print shape or reshapeing array when we use nupy library

if we need controll the numpy when we reshape using -1(row or col)
"""



print(multi.shape)

print (multi.reshape(2,6))
print(multi)


"""
how we achive slicing:

slicing syntax ===>[
row to row vanum 
give starting row and ending row 
for example we keed 2 and 3 row
1:3]

start ===> inclusive
end ====> exclusive


[start,end,step]

"""

slicinginput = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

print(slicinginput.ndim)
print(slicinginput[1,2])


matrix =np.array( [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(f'4*4 matrix skip 1 and last rows {matrix[1:3,1:3]}')



demo = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

bonus = np.array([5, 10, 15])

result = demo + bonus

print(f'print result when i use prodcast {result}')

grace_mark = np.array(
    
        [5]
    
)

print(f'shape of grace mark{grace_mark.shape}')

add_grace_mark = marks+grace_mark

print(f'add_grace_mark valur{add_grace_mark}')


weighted_score = np.array([0.3,0.3,0.4])

print(f'add and print weighted score using np.dot{np.dot(marks,weighted_score)}')

print(f'add and print weighted score using @{marks@weighted_score}')

arr = np.arange(12)
reshaped = arr.reshape(3, 4)

print(reshaped)

print(f'reshaped {reshaped}')



# load and creating csv
"""
we need to add the data array format and that value data type we need to change object
"""

employees = np.array([
    [1, "Arun", "Sales", 30000, "Chennai"],
    [2, "Priya", "HR", 45000, "Chennai"],
    [3, "Rahul", "IT", 60000, "Bangalore"],
    [4, "Divya", "IT", 75000, "Chennai"],
    [5, "Karthik", "Finance", 90000, "Mumbai"],
    [6, "Meena", "Sales", 52000, "Bangalore"],
    [7, "Suresh", "IT", 68000, "Chennai"],
    [8, "Anitha", "HR", 48000, "Mumbai"]
], dtype=object)


np.savetxt("employee.csv",employees,delimiter=",",fmt="%s",
           header="id,name,department,salary,location",
           comments=""
           )

print("employees.csv created successfully")

data = np.genfromtxt(
    "employee.csv",
    delimiter=" , ",
    dtype=str,
    skip_header=1
)

print(f"loaded csv {data}")


df = pd.read_csv("employee.csv")

# print header value

print(df.head())


#print info

print(f"info {df.info()}")


#print des
print(f"describe {df.describe()}")


#print name only

print(f'name {df["name"]}')

#print name and salary

print(f'name {df[["name","salary"]]}')


#print chennai employeess only
print(df.loc[df["location"] == "Chennai", "name"])

print(df.iloc[0:3, 1:3])



# Salary above 50000
high_salary = df[df["salary"] > 50000]
print("\n=== SALARY > 50000 ===")
print(high_salary)
print("Count:", len(high_salary))

# IT department employees
it_employees = df[df["department"] == "IT"]
print("\n=== IT EMPLOYEES ===")
print(it_employees)
print("Count:", len(it_employees))