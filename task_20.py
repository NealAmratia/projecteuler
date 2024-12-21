def factorial(n):
    """
    Calculate the factorial of a number n.
    
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

answer=factorial(100)

print("{} has {} digits".format(answer, len(str(answer))))

sum = 0

for i in range (len(str(answer))):
    sum += (int((str(answer))[i]))

print(sum)
    