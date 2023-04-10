# PYTHON FILE HANDLING

# Open File
file = open("pertemuan_5.txt", "rt")
print(file)

# Read file
# print(file.read())

# Readline
print(file.readline())
print(file.readline())

file.close()

# Write
file = open("pertemuan_5.txt", "a")
file.write("""Ini Sebuah Text File
Ini Baris Ke-2Now the file has new content!Now the file has new content!""")
file.close()

file = open("pertemuan_5.txt")
print(file.read())

# Remove File
import os
os.remove("pertemuan_5.txt")