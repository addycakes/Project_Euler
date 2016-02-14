'''
Problem 87
The smallest number expressible as the sum of a prime square, prime cube,
and prime fourth power is 28. In fact, there are exactly four numbers below fifty that
can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
'''

import math
import random

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes1=_known_primes
_known_primes2=_known_primes
_known_primes3=_known_primes
_known_primes1 += [x for x in range(5,7072, 2) if is_prime(x)]
_known_primes2 += [x for x in range(5,369, 2) if is_prime(x)]
_known_primes3 += [x for x in range(5,85, 2) if is_prime(x)]


nums = []
for a in _known_primes1:
    for b in _known_primes2:
        if (a**2 + b**3) > 50000000:break
        for c in _known_primes3:
            num = a**2 + b**3 + c**4
            if num > 50000000:
                break
            else:
                nums += [num]

print len(set(nums))

