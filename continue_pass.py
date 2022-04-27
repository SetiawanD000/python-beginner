# kontrol flow continue pass break

# pass -> data dummy tidak akan di eksekusi
# angka = 1

# while angka <12:
#     angka += 1
#     if angka == 3:
#         pass
#     print (f"aku angka ke {angka}")


# continue
angka = 0
print(f"angka {angka}")
while angka <7:
    angka += 1
    print (f"aku angka ke {angka}")
    if angka >= 3:
        print("Mantap")
        continue
    print("Okkay")
print("finish")

# braak
print(5*"="+"Break"+5*"=")
angka = 0
print(f"angka {angka}")
while angka <7:
    angka += 1
    print (f"aku angka ke {angka}")
    if angka >= 3:
        print("Mantap")
        break
    print("Okkay")
print("finish")