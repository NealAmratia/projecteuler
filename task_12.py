import math
# def triangle_numbers(n):
#     triangle_numbers = [1]
#     for i in range(2,n+1):
#         triangle_numbers.append(i+triangle_numbers[i-2])
#     return triangle_numbers

# def factors(n):
#     factors = []
#     for i in range(1,n+1):
#         if n%i == 0:
#             factors.append(i)
#     return factors

def nth_triangle_number(n):
    return int(n*(n + 1)/2)

# def factors_len(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             count += 1
#     return count

def factors_len(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)

divisors = 500

n = 0
i = 1

while n < divisors:
    t = nth_triangle_number(i)
    n = factors_len(t)
    i += 1

print("The value of the first triangle number to have over " + str(divisors) + " divisors is " + str(t) + ", with " + str(n) + " divisors")