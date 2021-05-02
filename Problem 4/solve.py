# Find the greatest among 3 values

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

# Condition checking

if (a>b and a>c):
    print("A is the greatest among the three values.")
elif (b>a and b>c):
    print("B is the greatest among the three values.")
else:
    print("C is the greatest among the three values.")