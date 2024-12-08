n = 1000

def sum_of_powers(n):
    power = 2**n
    power_str = str(power)
    l = list(power_str)

    for i in range(len(l)):
        l[i] = int(l[i])

    return(sum(l))

print(sum_of_powers(n))