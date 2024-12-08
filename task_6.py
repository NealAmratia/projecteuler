n = 100

def sum_of_sqaures(n):
    sosq_list = []
    for i in range(1,n+1):
        sosq_list.append(i**2)
    sosq = sum(sosq_list)
    return sosq

def square_of_sums(n):
    sum_of_numbers = 0
    for i in range(1,n+1):
        sum_of_numbers = sum_of_numbers+i
    sqos = sum_of_numbers**2
    return sqos

sosq = sum_of_sqaures(n)
sqos = square_of_sums(n)

print(sqos - sosq)