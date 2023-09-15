def factorial(n):
    """This is a recursive function
    to find the factorial of an integer"""

    if n==0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))


num = 0
print("The factorial of", num, "is", factorial(num))