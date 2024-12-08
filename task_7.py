n = 10001

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_num = []
p = 2

while len(prime_num) < n:
    if is_prime(p):
        prime_num.append(p)
    p = p+1

print(max(prime_num))
