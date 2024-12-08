
flist = [1, 2]
even_list = []

while flist[-1] + flist[-2] <= 4000000:
    flist.append(flist[-1] + flist[-2])

for i in range(len(flist)):
    if flist[i] % 2 == 0:
        even_list.append(flist[i])

print(even_list)
print(sum(even_list))
