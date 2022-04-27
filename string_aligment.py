# width and multiline

# data
data_nama = "ucup Sang Mawar"
data_umur = 18
data_tinggi = 178.9
data_nomor_kaos = 24

def garis(data):
    return print("\n"+5*"="+data+"="*5)

# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, kaos = {data_nomor_kaos}"
garis("Data String")
print(data_string)

# string multi line menggunakan brak line atau enter \n
data_multiline = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nkaos = {data_nomor_kaos}"
garis("Data Multiline")
print(data_multiline)

# string multiline dengan kutip triplents
data_multiline = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
"""
garis("Data Multiline dengan kutip 3")
print(data_multiline)