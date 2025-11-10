a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(a, "is the biggest of the given numbers")
elif b > a and b > c:
    print(b, "is the biggest of the given numbers")
else:
    print(c, "is the biggest of the given numbers")
