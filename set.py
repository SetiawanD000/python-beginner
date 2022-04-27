# set integer
myset = {1,2,3}
print(myset)

# set dengan fungsi set
myset = set([1,2,3])
print(myset)

# set data campuran int, string dan tuple
myset1 = {1,2,0,"python",(3,4,5)}
print(myset1)

# bila ada duplikasi set akan menghilangkan duplikasinya 
myset = {1,2,3,3,3,3,3}
print(myset)

# set tidak bisa berisi angota list
myset = {1,2,3,[4,5]}
print(myset)