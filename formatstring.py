# format string

# contoh generik
# string
nama = "elfas"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2000.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
bulat = 10
format_str = f"bilangan bulat = {bulat:d}"
print(format_str)

# ribuan
ribu = 100000000000
format_str = f"bilangan bulat = {ribu:,}"
print(format_str)

# bilangan bulat limit
angka = 2000.54231
format_str = f"angka = {angka:.2f}"
print(format_str)

# bilangan desimal depan nol
angka = 2000.54231
format_str = f"angka = {angka:08.2f}"
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = 10

format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# memformat persen
presentase = 0.045
format_perssen = f"format persen = {presentase:.2%}"
print(format_perssen)

# melakukan operasi aritmatika
harga = 1000
jumlah = 7
format_string = f"harga total = {harga*jumlah:,}"
print(format_string)

# format angka lain
angka = 255
format_binnary = f"binnary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binnary)
print(format_octal)
print(format_hex)