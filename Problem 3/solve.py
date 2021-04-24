# Find the factorial of a number using the recursive function

def factorial(num):
    # This will be our recursive function
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
    

# Find the factorial 

num = int(input("Enter a number: "))

# condition checking

if num < 0:
    print("Factorial value cannot be found for the negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is:", factorial(num))