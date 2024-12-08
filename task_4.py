prod = []
palindrome_prod = []

for i in range(1,1000):
    for j in range(1, 1000):
        prod.append(i*j)

prod = list(set(prod))

for i in range(len(prod)):
    if prod[i] == int((str((prod[i])))[::-1]):
        palindrome_prod.append((prod[i]))

print(max(palindrome_prod))