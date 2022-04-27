from ctypes.wintypes import HENHMETAFILE


nama_pertama = "heni"
nama_kedua = "is"
nama_ketiga = "my wife"

# menyambung string
nama_lengkap = nama_pertama+nama_kedua+nama_ketiga
print(nama_lengkap)

# menghitung string
nama_jumlah = len(nama_lengkap)
print("panjang nama "+str(nama_jumlah))

# mengecek apakah ada komponen char di string
d = "i"
status = d in nama_lengkap
print(d+" ada di " + nama_lengkap + " " + str(status))

# mengulang string
print("heni "*10)

# indexing
print("index ke 0 adalah "+nama_lengkap[0])
print("index ke 0 adalah "+nama_lengkap[-1])
print("index ke 0 adalah "+nama_lengkap[-2])
print("index ke 0 - 3 adalah "+nama_lengkap[0:4])
print("index ke 0 - 10 dengan increment adalah "+nama_lengkap[0:12:2])


# item paling kecil & besar nilanya
print("paling kecil : "+min(nama_lengkap))
print("paling besar : "+max(nama_lengkap))

# operator dalam bentuk method
data = "heni is my dream"
jumlah = data.count("e")
print("jumlah e dalam data adalah : "+str(jumlah))
