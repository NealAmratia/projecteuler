def prod_list(n):
    prod = []
    for i in range(1,n):
        for j in range(1,n):
            prod.append(i*j)
    prod = list(set(prod))
    return prod

def is_palindrome(n):
    if n == int((str(n))[::-1]):
        return True
    else:
        return False

prod = prod_list(1000)
palindrome_prod = []

for i in range(len(prod)):
    if is_palindrome(prod[i]):
        palindrome_prod.append((prod[i]))

print(max(palindrome_prod))
