# CLASS AND OBJECT
# Membuat Class
# class myClass:
#     nama = "NurHabib"
#
# # Membuat Object
# habib = myClass()
# print(habib.nama)
#
# # Inisiaisasi / Constructor & Self Parameter
# class Person():
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur
#         self.mahluk = "manusia"
# class Person2():
#     nama = "NurHabib"
#     umur = 17
#     def lari(self):
#         print("Lari")
#     def jalan(Person):
#         print("Jalan")
#
# NurHabib = Person("NurHabib", 17)
# print(NurHabib.nama)
# print(NurHabib.umur)
# print(NurHabib.mahluk)
#
# # Method Class
# class Manusia():
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur
#
#     def lari(self):
#         print("Lari")
#
# del NurHabib
# NurHabib = Manusia("NurHabib2", 17)
# NurHabib.lari()
#
# # Hapus Object
# del NurHabib
#
# # Mengubah Nilai Pada Object
# NurHabib = Manusia("NurHabib", 16)
# print(NurHabib.nama)
# print(NurHabib.umur)
# NurHabib.umur = 17
# print(NurHabib.nama)
# print(NurHabib.umur)
#
# # Turunan
# class Student(Manusia):
#     def __init__(self, nama, umur, nis):
#         super().__init__(nama, umur) # Supaya tidak perlu mengulang penulisan inisialisasi dan dapat menambah atribut
#         self.nis = nis
#     def belajar(Student): # Parameter Student = self
#         print("Belajar")
#
# adi = Student("adi", 17, nis=19832)
# print(adi.nama)
# adi.belajar()
#
# for i in range(10):
#     print()

# STUDY CASE
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = "tertutup"
        self.mobil = "mati"

    def membukPintu(self):
        if self.pintu == "tertutup":
            print("Pintu Berhasil Dibuka")
            self.pintu = "terbuka"
        else:
            print("Pintu Telah Terbuka")

    def menutupPintu(self):
        if self.pintu == "terbuka":
            print("Pintu Berhasil Ditutup")
            self.pintu = "tertutup"
        else:
            print("Pintu Telah Tertutup")

    def menyalakanMobil(self):
        if self.mobil == "mati":
            print("Mobil Berhasil Dinyalakan")
            self.mobil = "menyala"
        else:
            print("Mobil Sudah Menyala")


    def mematikanMobil(self):
        if self.mobil == "menyala":
            print("Mobil Berhasil Dimatikan")
            self.mobil = "mati"
        else:
            print("Mobil Sudah Mati")

mobilku = Car("toyota", 2021)

mobilku.membukPintu()
mobilku.membukPintu()
mobilku.membukPintu()
mobilku.menutupPintu()
mobilku.menutupPintu()
mobilku.menutupPintu()
mobilku.menyalakanMobil()
mobilku.menyalakanMobil()
mobilku.menyalakanMobil()
mobilku.mematikanMobil()
mobilku.mematikanMobil()
mobilku.mematikanMobil()
