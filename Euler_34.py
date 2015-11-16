import math
'''
Euler Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''

def factorialDigits(num):
    #returns sum of digits
    factorialSum = 0
    
    for digit in str(num):
        factorialSum += math.factorial(int(digit))

    return factorialSum

allSum = 0
for i in range(3,1000000):
    if i == factorialDigits(i):
        allSum += i

print allSum
