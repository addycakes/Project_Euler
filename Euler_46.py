'''

Euler Problem 46

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def canBeGoldbach(num):
    for prime in primes:
        pSum = math.sqrt((num - prime) / 2.0) 
        if pSum.is_integer():
            return True

    return False

primes = []
for i in range(1,10000000):
    if i % 2 == 0:
        continue
    else:
        if is_prime(i):
            primes += [i]
        if canBeGoldbach(i):
            continue
        else:
            break

print i
