a = int(input("Enter the first value : "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

# condition checking

if (a>b and a>c):
    print(a, "is the greatest value among the three values.")
elif (b>a and b>c):
    print(b, "is the greatest value among the three values.")
else:
    print(c, "is the greatest value among the three values.")