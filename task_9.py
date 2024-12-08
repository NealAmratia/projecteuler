for a in range(1, 500):
    for b in range(a+1, 500):
        
        # Compute c
        c = 1000 - a - b
        
        # Check if a^2 + b^2 = c^2
        if a**2 + b**2 == c**2:
            
            # We found a Pythagorean triplet!
            print("a =", a)
            print("b =", b)
            print("c =", c)
            
            # Compute the product abc
            print("abc =", a*b*c)
            
            # Exit the loops
            break
    else:
        continue
    break