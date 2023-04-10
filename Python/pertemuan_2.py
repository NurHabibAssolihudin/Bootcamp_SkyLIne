# PYTHON LIST
ini_list = ["list1", "list2", "list3"]

# Index
print(ini_list[0])

# Range Index
print(ini_list[-3:-1])

# Change Items
ini_list[0] = "list"
print(ini_list)

# Range Change Items
ini_list[1:3] = ["list pertama", "list ke dua"]
print(ini_list)

# Insert Items
ini_list.insert(0, "list ke 0")
print(ini_list)

# Append Items
ini_list.append("list ke tiga")
print(ini_list)

# Extend List
ini_list2 = ["list ke-5", "list terakhir"]
ini_list.extend(ini_list2)
print(ini_list)
print(ini_list2)

# Remove List
ini_list.remove("list ke-5")
print(ini_list)

# Remove
# remove(), pop(), del => del ini_list[0], clear()

# Python Loop List
# Foor loop
print()
print("For loop")
for i in ini_list:
    print(i)
for i in range(len(ini_list)):
    print(ini_list[i])

# While loop
print()
print("While loop")
i = 0
while i < len(ini_list):
    print(ini_list[i])
    i += 1

# List comprehension
print()
print("List comprehension")
[print(x) for x in ini_list]

# STUDY CASE
# 1
thislist = ["apple", "banana", "mango"]
thislist.remove("banana")
assert(thislist) == ["apple", "mango"]

# 2
thislist.append("kiwi")
assert(thislist) == ["apple", "mango", "kiwi"]

# 3
new_list = ["apple", "apple", "apple", "apple", "mango", "kiwi", "apple", "apple", "apple", "apple"]
assert(new_list[4:6]) == ["mango", "kiwi"]

# 4
new_list = ["apple", "apple", "apple", "apple", "mango", "kiwi", "apple", "apple", "mango", "kiwi", "apple", "apple"]
list_baru = []
for i in new_list:
    if i != "apple":
        list_baru.append(i)
assert(list_baru) == ["mango", "kiwi", "mango", "kiwi"]

# Sort Array
list1 = [1, 2, 4, 3, 5]
list1.sort()
print(list1)

# Reverse Array
list1.reverse()
print(list1)

# STUDY CASE
# 1
list1 = [1, 4, 5, 6, 2, 4]
assert([x for x in list1 if x != 4]) == [1, 5, 6, 2]
assert([x for x in list1 if x == 4]) == [4, 4]

# Copy List
list2 = list1.copy()
list2.remove(4)
print(list1, list2)

# STUDY CASE
list1 = [1, 4, 5, 7]

list3 = list1.copy()
list3.remove(7)

assert(list3) == [1, 4, 5]
assert(list1) == list1

# Python Tuple
thistuple = ("apple", "banana", "cherry")

# unpacking tuple
buah1, buah2, buah3 = thistuple
print(buah1, buah2, buah3)

# cara mengubah nilai tuple
print(thistuple)
x = list(thistuple)
x.append("kiwi")
thistuple = tuple(x)

print(thistuple)

# Dictionarys
cars = {
    "brand" : "honda",
    "product" : "civic"
}

print(cars["brand"])
print(cars.keys())

# STUDY CASE
assert(list(cars.keys())[1]) == "product"

# Get Dictonarys
# cars["year"] error dan dapat menyebabkan kerusakan system
cars.get("year", None)

# Update
cars.update(
    {
        "year" : 2023,
        "key2" : 2005
    }
)

print(cars)

# PYTHON FUNCTION
# Tidak mengembalikan nilai = prosedur
# mengembalikan nilai = method
def myFunc():
    print("Hello Python Function")
myFunc()

# Parameter
def myFuncPar(nama):
    print("Halo " + nama)
myFuncPar("NurHabib")

# Return Value
def myFuncRet():
    nama = "NurHabib"
    return nama
nama = myFuncRet()
print("Halo " + nama)

# Arbitary Argument / Array Parameter
def myFuncArb(*nama):
    print(nama)
    for i in nama:
        print("Halo " + i)
myFuncArb("Habib", "Agung", "Nandan")

# Keyword Argument
def myFrend(frend1, frend2, frend3="friend3"):
    print(frend1)
    print(frend2)
    print(frend3)
myFrend(frend1="Agung", frend3="Adi", frend2="Aji")

myFrend("friend1", "friend2")

# Default Parameter
def makanan(makanan1 = "Nasi Goreng", makanan2 = "Bakso", makanan3 = "Mie Ayam"):
    print(makanan1, makanan2, makanan3)
makanan()

# Arbitary Keyword Argument
def fullName(**fulName):
    print(fulName)
    print("First name is " + fulName["fname"])
    print("Last name is " + fulName["lname"])
fullName(fname="NurHabib", lname="Assolihudin", age=17)

# Passing a List as an Argument

# STUDY CASE
# 1
def multiply_by_two(a):
    return a * 2

assert(multiply_by_two(3)) == 6

# 2
def multiply_by_x(a, x = 2):
    return a * x

assert(multiply_by_x(3)) == 6
assert(multiply_by_x(3, 1)) == 3

# Input
user_input = input("Masukan Nama : ")
print("Nama User Adalah " + user_input)

# Break
i = 0
while True:
    if i == 0:
        break

# STUDY CASE
for i in range(5):
    print()
"""
Enter the number of students in your class: 3
Enter the name of student 1: Emil
Enter the grades of student 1 (comma-separated): 85,90,92
Enter the name of student 2: Tobiaz
Enter the grades of student 2 (comma-separated): 78,80,84
Enter the name of student 3: Refsnes
Enter the grades of student 3 (comma-separated): 92,95,98

Average grades:
Alice: 89.0
Bob: 80.67
Charlie: 95.0
"""

students = input("Enter the number of students in your class: ")
student = []
# name = []
# total_grade = []

def totalGrades(grades):
    grade = 0
    grades = grades.split(",")
    for i in grades:
        grade += float(i)
    grade = grade/len(grades)
    return grade

for i in range(int(students)):
    name = input("Enter the name of student " + str(i+1) + ": ")
    grades = input("Enter the grades of student " + str(i+1) + " (comma-separated): ")
    student.append(
        {
            "nama" : name,
            "grade" : grades,
            "averange_grade" : totalGrades(grades)
        }
    )
    # total_grade.append(totalGrades(grades))

print()
print("Averange grades:")
for z in student:
    print(z["nama"], ":", z["averange_grade"])
