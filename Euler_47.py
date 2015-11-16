'''
Euler Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?

'''
import math

def is_prime(num):

    for i in range(2, (int(math.sqrt(num)))+1):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(2,1000):
    if is_prime(i):
        primes += [i]
        
def primeFactorization(n):
    factors = []
    prime_potential = 0
    global primes
    while n not in primes and n != 1:
        prime_potential = n
        for prime in primes:
            if n % prime == 0:
                factors += [prime]
                n = n / prime
                break
        if (prime_potential == n):
            primes += [n]
        #print "looping " + str(n)

    factors += [n]
    return factors

def countUniqueFactors(n):
    digits = []
    ud = 0
    for digit in n:
        if digit in digits:
            continue
        else:
            digits += [digit]
            ud += 1

    return ud

i = 1
factor_counts = {}
while i <1000000:
    try:
        distinct_factors1 = factor_counts[i]
    except KeyError:
        distinct_factors1 = countUniqueFactors(primeFactorization(i))
        factor_counts[i] = distinct_factors1
    try:
        distinct_factors2 = factor_counts[i+1]
    except KeyError:
        distinct_factors2 = countUniqueFactors(primeFactorization(i+1))
        factor_counts[i+1] = distinct_factors2
    try:
        distinct_factors3 = factor_counts[i+2]
    except KeyError:
        distinct_factors3 = countUniqueFactors(primeFactorization(i+2))
        factor_counts[i+2] = distinct_factors3
    try:
        distinct_factors4 = factor_counts[i+3]
    except KeyError:
        distinct_factors4 = countUniqueFactors(primeFactorization(i+3))
        factor_counts[i+3] = distinct_factors4

    if distinct_factors1 == 4 and distinct_factors2 == 4 and  distinct_factors3 == 4 and distinct_factors4 == 4:
        print i, i+1, i+2, i+3
        break
    i += 1
