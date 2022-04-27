# operator dalam bentuk methon

# merubah case dari string

# merubah semua ke uppercase

salam = "cantik"
print("normal : "+salam)

salam = salam.upper()
print("upper : "+salam)

# merubah ke lower
alay = "Aku KECE ABIZZZZZZZZ"
print("alay : "+alay)
alay = alay.lower()
print("alay lower : "+alay)
print("="*20)
# pengecekan lower case
salam1 = "sist"
apakah_lower = salam1.islower()
print(salam1+" is lower = "+str(apakah_lower))
apakah_upper = salam1.isupper()
print(salam1+" is upper = "+str(apakah_upper))

# isalpha() = untuk pengecekan semua huruf
# isalnum() = huruf dan angka
# isdecimal() = angka saja
# isspace() =spasi,tab, new line \n
# istitle() = semua kata di awali huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul+" is title = "+str(cek_judul))

# pengecekan komponen starswith() endswith() <---- keren
cek_start = "Sang Bujangan".startswith("Sang") #pengecekan awal kata
print("start = "+str(cek_start))
cek_end = "Sang Bujangann".endswith("Bujangann") #pengecekan akhir kata
print("End = "+str(cek_end))



# pengabungan komponen join(), split()
pisah = ['aku','sayang','kamu']
gabung = ' '.join(pisah)
print(gabung)
pisah_lagi = gabung.split(' ') #mengembalkan ke list(array)
print(pisah_lagi)