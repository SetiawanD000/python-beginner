# dictionary merupakan tipe data yang anggotanya terdiri dari pasangan dan value
data = {
    "satu" : "kelas 1",
    "dua" : "kelas 2",
    "tiga" : "kelas 3",
    "empat" : "kelas 4",
}

print(data)
print(len(data))
print(f"type dari data : {type(data)}")

# akses per item
print(data['satu'])

# akses dengan for
for i in data:
    print(f"{i} => {data[i]}")