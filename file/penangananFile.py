# membuka file
# membaca file
# f = open("test.txt")
# membaca baris
# print(f.read(4))
# # /membaca yang berikutnya
# print(f.read(4))
# # /membaca yang berikutnya dan seterusnya
# print(f.read())


# membaca perbaris
# print(f.readline())

# membaca seluruh text
# print(f.readlines())

# menulis
f = open("test.txt",'w')
f.write("test 5\n")
f.write("test 6\n")
f.write("test 7\n")
f.write("test 8\n")

# menutup file
f.close()