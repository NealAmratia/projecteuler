n = 2000000

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_sum = 2

for i in range(3,n):
    if is_prime(i):
        prime_sum = prime_sum + i

print(prime_sum)