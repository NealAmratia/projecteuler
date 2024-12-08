i = 2
n = 600851475143

factors_list = []
prime_factors_list = []

for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        factors_list.append(i)

def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

for i in range(len(factors_list)):
    if is_prime(factors_list[i]):
        prime_factors_list.append(factors_list[i])

print(prime_factors_list)
print(max(prime_factors_list))