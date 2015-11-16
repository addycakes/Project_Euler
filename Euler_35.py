import math

'''
Euler Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def isCirclePrime(num):
    circle = str(num)
    for i in range(len(circle)):
        if not is_prime(int(circle)):
            return False
            
        circle = circle[1:] + circle[0]
        
    return True

count = 0
for i in range(2,1000000):
    if isCirclePrime(i):
        count += 1

print count
    
