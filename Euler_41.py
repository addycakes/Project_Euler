'''
Project Euler 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
import math
import itertools

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def hasPandigitalPrime(num):
    digits = range(1,num+1)
    combinations = itertools.permutations(digits,len(digits))
    pandigital_primes = [0]
    
    for comb in combinations:
        toNumber = "".join(map(str, comb))
        if int(toNumber) % 2 == 0:
            continue
        if is_prime(float(toNumber)):
            pandigital_primes += [int(toNumber)]

    return max(pandigital_primes)

maxPrime = 0
for i in range(3,10):
    value = hasPandigitalPrime(i)
    if value > 0:
        if value > maxPrime:
            maxPrime = value

print maxPrime
