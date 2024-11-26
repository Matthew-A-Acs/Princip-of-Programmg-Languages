# Python Homework 1
# Matthew Acs
# COP 4020

# (1)  Print “Hello World” 
print("Hello World")

print("------------------------------------- 1")
# (2)  Save your age to a variable called “age” 
age = 18

print("------------------------------------- 2")
# (3)  Print “Hello World, I’m (age variable) today.” 
print("Hello World, I’m " + str(age) + " today.")

print("------------------------------------- 3")
# (4)  Print “hello world” in all upper case using a python function to alter it 
print("hello world".upper())

print("------------------------------------- 4")
# (5)  Save any decimal in a variable called a. 
a = 3.1415

print("------------------------------------- 5")
# (6)  Cast a into an int and save it as b. 
b = int(a)

print("------------------------------------- 6")
# (7)  Cast a into a string and save it as c.
c = str(a)

print("------------------------------------- 7")
# (8)  Print each variable and its type. 
print(a)
print(type(a))
print("")

print(b)
print(type(b))
print("")

print(c)
print(type(c))
print("")

print("------------------------------------- 8")
# (9)  Create a tuple of your favorite things to eat and print it. 
food = ("lobster", "pizza", "soup", "pancakes", "omelette")
print(food)

print("------------------------------------- 9")
# (10)  Create a dictionary named ‘classes’ with the name of the 
# classes you are taking as the keys and the professors names as the 
# values. 
classes = {'programming': 'Dr. Huang', 'biochemistry': 'Dr. Haces', 'AI': 'Dr. Marques', 'ED1': 'Dr. Zhuang'}

print("------------------------------------- 10")
# (11)  Print the dictionary and tuple.
print(classes)
print(food)

print("------------------------------------- 11")
# (12)  Create a list called “whole” and put every number in it from 1 - 
# 100 
whole = []
for i in range(1, 101):
    whole.append(i)

print("------------------------------------- 12")
# (13)  Create 4 empty lists called ‘div2’, ‘div3’, ‘div4’, and ‘div5’ 
div2 = []
div3 = []
div4 = []
div5 = []

print("-------------------------------------- 13")
# (14)  Create a loop that examines each number from 1 to 100 and: 
#   (a)  If it is divisible by 2, put it in div2 
#   (b)  If it is divisible by 3, put it in div3 
#   (c)  If it is divisible by 4, put it in div4 
#   (d)  If it is divisible by 5, put it in div5 
for x in whole:
    if x % 2 == 0:
        div2.append(x)
    if x % 3 == 0:
        div3.append(x)
    if x % 4 == 0:
        div4.append(x)
    if x % 5 == 0:
        div5.append(x)

print("-------------------------------------- 14")
# (15)  Print all 5 of these lists 
print(whole)
print("")
print(div2)
print("")
print(div3)
print("")
print(div4)
print("")
print(div5)

print("-------------------------------------- 15")
# (16)  Create a new list called “divOver5” 
divOver5 = []

print("-------------------------------------- 16")
# (17)  Create a new loop that goes through each number 1 through 
# 100 and appends it to divOver5 if it is NOT IN div2 or div3 or div4 or 
# div5 
#   (a)  You must use logical operators here. 
for x in whole:
    if (x not in div2) and (x not in div3) and (x not in div4) and (x not in div5):
        divOver5.append(x)

print("-------------------------------------- 17")        
# (18)  Print divOver5 
print(divOver5)

print("-------------------------------------- 18")
# (19)  Create a function called exp3 that takes an int x, raises it to the 
# third power.  Create a string in the function that says “x^3 = “ and 
# concatenate x onto the end of the string.  Now return the string from 
# the function.  Call the function exp3 and print what it returns.
def exp3(x):
    x = x**3
    result = "x^3 = "
    result = result + str(x)
    return (result)
    
print(exp3(2))

print("-------------------------------------- 19")
# (20)  Iterate through the classes dictionary and print the keys 
for x in classes:
    print(x)

print("-------------------------------------- 20")
# (21)  Iterate through the classes dictionary and print the values 
for x in classes:
    print(classes[x])

print("-------------------------------------- 21")    
#  Extra Points:   Create a class called Student that has the properties:  
#  name (holds student name) 
#  age (holds student age) 
#  birthmonth (hold students birthmonth) 
#   
#  A count variable exists that is set to 0 (see lecture) and upon each 
#  call to the class this variable increments 
# 
#  2 functions in the class:  displayName which returns the name of the 
#  student and displayBirthmonth which returns the birth month of the student 
# 
#  Now create 3 students, use whatever data you want.   
#  Call displayName() on student1 
#  Call displayBirthmonth() on student2 
#  print the student count 
class Student:
    studentCount = 0 
    
    def __init__(self, name, age, birthmonth):
        self.name = name
        self.age = age
        self.birthmonth = birthmonth
        Student.studentCount += 1
        
    def displayName(self):
        print(self.name)
        return self.name
        
    def displayBirthmonth(self):
        print(self.birthmonth)
        return self.birthmonth

student1 = Student("Albert", 19, "March")
student2 = Student("Bob", 20, "April")
student3 = Student("Charlie", 21, "May")

student1.displayName()
student2.displayBirthmonth()
print(Student.studentCount)

print("-------------------------------------- Extra Credit")    

