from ast import operator
from email.errors import HeaderMissingRequiredValue


print(5*"=")
print("Kalkulaor sederhana")
print(5*"="+"\n")

angka1 = float(input("Masukkan angka pertama? "))
angka2 = float(input("Masukkan angka kedua? "))
operator = input("Masukkan operator +-*/ :")

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1-angka2
    print(f"hasil {angka1} - {angka2} = {hasil}")
elif operator == "/":
    if angka2 == 0:
        print("pembagi tidak boleh nol !!!!!")
        print(f"hasil {angka1} / {angka2} ")
    else:
        hasil = angka1 / angka2
        print(f"hasil {angka1} / {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil {angka1} *9 {angka2} = {hasil}")
else:
    print("Masukkan angka atau operator yang bener dong gaes")