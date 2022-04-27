# date and time latihan

import datetime as dt


def garis(data):
    return print("\n"+5*"="+data+"="*5)
# data lengkap sekarang
x = dt.datetime.now()
garis("Data Tanggal Sekarang")
print(x)

# data lengkap tahun
garis("Data tahun Sekarang")
print(x.year)

# data hari ini
hari_ini = dt.date.today()
garis("Data Hari Sekarang")
print(f"hari ini {hari_ini:%a} tanggaal {hari_ini}")

# data tanggal input
tanggal = dt.date(2000,9,23)
garis("Data tanggal Input")
print(tanggal)