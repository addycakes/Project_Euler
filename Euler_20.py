'''
Euler Problem 20
'''

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i

    return product

def sumDigits(n):
    s = str(n)
    NumSum = 0

    for d in s:
        NumSum += int(d)

    return NumSum


print sumDigits(factorial(100))
