# import example as e
# print(e.hitung.__doc__)
# a = 10
# b = 35
# c = 67
# d = 76

# hitung_a = e.hitung(a)
# print(hitung_a)
# hitung_ab = e.hitung(a,b)
# print(hitung_ab)

from example import hitung as e
import math

print(e.__doc__)
a = 10
b = 35
c = 67
d = 76

hitung_a = e(a)
print(hitung_a)
hitung_ab = e(a,b)
print(hitung_ab)


print("nilai pi adalah :",math.pi)