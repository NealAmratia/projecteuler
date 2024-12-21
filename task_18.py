# Read the triangle data from a file
with open("task_18.txt", "r") as file:
    data = file.read()

# Convert to a 2D array
pyramid = [list(map(int, line.split())) for line in data.strip().split("\n")]

# Repeat until only one row is left
while len(pyramid) > 1:
    # Get the last two rows
    slr = pyramid[-2]  # Second last row
    lr = pyramid[-1]   # Last row
    
    # Create a new row by combining slr and lr
    nlr = [0] * len(slr)
    for i in range(len(slr)):
        nlr[i] = max(slr[i] + lr[i], slr[i] + lr[i + 1])
    
    # Replace the last two rows with the new row
    pyramid = pyramid[:-2]  # Remove the last two rows
    pyramid.append(nlr)     # Add the new row

# Print the final result
print(pyramid[0][0])  # The maximum total