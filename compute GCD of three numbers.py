import math

# Get three comma-separated numbers from the user
e1, e2, e3 = input("Enter 3 numbers separated by commas: ").split(',')

# Convert to integers
e1 = int(e1)
e2 = int(e2)
e3 = int(e3)

# Compute the GCD (greatest common divisor)
result = math.gcd(math.gcd(e1, e2), e3)

# Display the result
print(f"GCD of {e1}, {e2}, {e3} = {result}")
