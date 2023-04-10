# Variable
nama = "NurHabib" # penulisan variable biasa
nama = str("NurHabib") # bisa digunakan untuk lebih yakin terhadap tipe data
print(type(nama)) # built-in function ini digunakan untuk melihat tipe dari sebuah data yang tersimpan dalam variable

# Many Value For Many Variable
nama_saya, nama_temen = "NurHabib Assolihudin", "Agung Muhammad Yoransah" # value pertama akan masuk ke dalam vriable pertama, dan begitu pula value ke dua
print(nama_saya)

# Collection / List
teman = ["Agung", "Fahril", "Nandan"]
teman = list(("Agung", "Fahril", "Nandan"))
teman1, teman2, teman3 = teman # cara ini digunakan untuk memasukan nilai array pada masing-masing variable, sesuai urutan
print(teman)

# Print
print(nama, nama_saya, teman) # digunakan untuk menampilkan lebih dari 1 variable
print(1+2)

# Global Variable
x = 12 # variable ini dapat diakses oleh seluruh lingkup kerja
def myfunc():
    x = 13 # variable ini hanya b=dapat diakses oleh fungcion dan yang ada di dalamnya
    print(x)
myfunc()
print(x) # yang akan ditampilkan adalah variable (x) yang berada di luar function

# PYTHON STRINGS

# String yang diawali, dan diakhiri dengan tanda ("""), maka string tersebut dapat ditulis lebih dari 1 baris dan akhir baris-pun ikut tampil
string_panjang = """Ini dapat digunakan
untuk menulis string
yang memiliki lebih dari 1 baris"""
print(string_panjang)

# String Sama Dengan Array
print(nama[1])
for i in "NurHabib":
    print(i)
print("Panjang Variable Nama Adalah " + str(len(nama)) + " Huruf")

# Check Strings
print("Habib" in nama)
if "Habib" in nama:
    print("Yes, Habib is in nama")
else:
    print("No, Habib is not in nama")

# Modify String

# Upper & Lower Case
print(nama.upper())
print(nama.lower())

# Strip
nama = " NurHabib "
print(nama)
print(nama.strip())

# Split
print(nama_saya.split(" "))
print(nama.split("H"))

# Study Case
# 1
def sum_int_or_str(a, b):
    return int(a) + int(b)

assert(sum_int_or_str(1, '2')) == 3

# 2
def get_second_character(a):
    # Get second character, if only 1 character return 0
    if len(a) > 1:
        return a[1]
    else:
        return 0
assert(get_second_character("ab")) == "b"
assert(get_second_character("a")) == 0

# 3
car = {
    "brand" : "Toyota",
    "year" : 2022
}

assert(car["brand"]) == "Toyota"

# 4
cars = [
    {
        "brand" : "Toyota"
    },
    {
        "brand" : "Honda",
        "product" : [
    "civic"
]
    }
]

assert(cars[1]["product"][0]) == "civic"

# 5
raw_cars = "toyota,honda,indiacar"
raw_cars = raw_cars.upper()

assert(raw_cars.split(",")) == ["TOYOTA", "HONDA", "INDIACAR"]

# 6
raw_cars = "toyota,honda,indiacar,indiacar,indiacar"
# def sortir(a):
#     a = a.split(",")
#     for i in a:
#         if a[i] == a[i + 1]:
#             a[i].remove()
# raw_cars = raw_cars.split()
# raw_cars = set(raw_cars)
# raw_cars = list((raw_cars))
#
# assert(raw_cars) == ['toyota', 'honda', 'indiacar']

# PYTHON OPERATOR

# Aritmathic Operator
# +.-,/,*,**,%

# Assignment Operator

# Comparison Operator

# Logical Operator

# Identity Operator
# is, is not

# Membership Operator
# in, not in

# Betwise Operator
# &, |, !

# STUDY CASE
raw_cars = "toyota,honda,indiacar,indiacar,indiacar"
raw_cars = raw_cars.split(",")
raw_cars = set(raw_cars)
raw_cars = len(raw_cars)
assert(raw_cars) == 3