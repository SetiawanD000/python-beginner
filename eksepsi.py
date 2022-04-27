import sys

lists = ['a',0.4,7,3]

for i in lists:
    try:
        print("masukan :",i)
        r =1/int(i)
        break
    except:
        print("Upss...", sys.exc_info()[0], "terjadi")
        print("Masukan berikutnya")
        print()
print("Kembalikan dari ",i, " =",r)