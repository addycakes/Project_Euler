import math

'''
Euler Problem

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def areDigitsPrime(num):
    digits = str(num)
    
    for i in range(len(digits)):
        if not is_prime(int(digits[i:])):
            return False
        if not is_prime(int(digits[:len(digits)-i])):
            return False

    return True

Trunc_Primes = []
for j in range(10, 1000000):
    if areDigitsPrime(j):
        Trunc_Primes += [j]

print Trunc_Primes
print sum(Trunc_Primes)
