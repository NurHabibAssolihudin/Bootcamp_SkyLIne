# PYTHON DATETIME
# Import Librery

import datetime

# Date
date = datetime.datetime.now()
print(type(date))

# Creating Date Object
now = datetime.datetime(2023, 4, 3)
print(now)

# strftime
print(date.strftime("%d/%m/%Y"))

# STUDY CASE
# 1
arr_1 = [5, 78, 2, 0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78

def minimal(arr):
    arr.sort()
    return arr[0]

def maximal(arr):
    arr.sort()
    return arr[len(arr) - 1]

assert(minimal(arr_1)) == 0
assert(maximal(arr_1)) == 78

# 2
assert(5**5) == 3125

# Try Execpt
try:
    print(z)
except:
    print("Variable belum didefinisikan")

# Other Execpt
try:
    print(z)
except NameError:
    print("Variable is not defined")
except:
    print("Another error")

# Else
try:
    print(x)
except:
    print("Variable is not defined")
else:
    print("Ok")

# Finaly
try:
    print(y)
except:
    print("Variable is not defined")
else:
    print("Ok")
finally:
    print("Try is done")

# Rise an execption
x = -1
if x > 0:
    raise Exception("Blabla")

# Try Execpt
try:
    f = open("pertemuan_5.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Cant Write")
    finally:
        f.close()
except:
    print("Cant Open File")