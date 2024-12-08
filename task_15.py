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


"""
Combinatorics solution for a grid size m x n
solution = (m+n)! / (m!).(n!)
"""

m = 20
n = 20

solution = int((factorial(m+n))/((factorial(m))*(factorial(n))))

print(solution)