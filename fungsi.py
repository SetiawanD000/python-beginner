def sapa(nama):
    """fungsi ini untuk menyapa seseorang"""
    return (f"Hi, {nama}. Apa kabar?")

# pemanggilan fungsi
print(sapa("Heni"))
# fungsi bisa di masukkan dalam variabel 
agus = sapa("agus")
print(agus)

# pangil deskripsi fungsi
# dokumentasi bisa ditulis didalam fungsi dan diapit 3 tanda quotes
komentar = sapa.__doc__
print(komentar)

# /urutan parameter tidak menjadi masalah
def info(nama,usia = 17):
    """fungsi => menampilkan info yang dimasukan"""
    return (f"Hay, {nama} usia kamu {usia}")
heni = info(usia = 20, nama="Heni")
elfas = info( nama="Ela")
print(elfas)

# fungsi dengan argumen tak terhingga
def cinta(arg1,*vartuple):
    """fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan"""
    print("Outpunya adalah :")
    print(f"cinta pertamaku : {arg1}")
    for i in vartuple:
        print(f"aku cinta {i}")
# panggil dengan satu argument
cinta(10)

# panggil dengan banyak arumen
cinta("dia","nima","Mia","Sofia")