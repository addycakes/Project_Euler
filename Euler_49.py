'''
Euler Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def isPermutation(l):
    for num in l:
        string = str(num)
        for num2 in l:
            string2 = str(num2)
            for digit in string2:
                if digit not in string:
                    return False

    return True

for i in range(1000,10000):
    term1 = i
    if is_prime(term1):
        term2 = i + 3330
        if is_prime(term2):
            term3 = term2 + 3330
        if is_prime(term3):
            if isPermutation([term1,term2,term3]):
                print term1
                print term2
                print term3

    
