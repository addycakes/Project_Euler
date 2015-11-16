'''
Euler Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''
import math
import random
 
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

primes = []
primeSums = []
r = 1000000
finished = False
for i in range(2,r):
    if i == 2 or is_probable_prime(i):
        primes += [i]

        if not finished:
            pSum = 0
            for p in primes:
                pSum += p
            if pSum < r:
                primeSums += [pSum]
            else:
                finished = True
        
print "primes done"

maxP = 0
maxLen = 0
for i in range(len(primeSums)):
    for j in range(1, len(primeSums)+1):
        k = len(primeSums) - j

        if primeSums[k] in primes:
            if k-i > maxLen:
                maxLen = k-i
                maxP = primeSums[k]
            
        if primeSums[k] - primeSums[i] in primes:
            if k-i > maxLen:
                maxLen = k-i
                maxP = primeSums[k] - primeSums[i]
                print maxP            
