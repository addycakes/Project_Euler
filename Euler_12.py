'''
Project Euler #12
Highly Divisible Triangle Number

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

'''

def getTriangleNumber(n):
    # nth triange number interested in
    # n of 7 returns 28
    t_sum = 0
    for i in range(1,n+1):
        t_sum += i

    return t_sum

def primeFactorization(n):
    exponents = {}
    factors =  reduceFactor(n)
    for factor in factors:
        try:
            exponents[factor] += 1
        except KeyError:
            exponents[factor] = 1

    total_factors = 1
    for exponent in exponents:
        num = exponents[exponent] + 1
        total_factors *= num

    return total_factors
    
def reduceFactor(n):
    factors = []
    prime_potential = 0
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
              79,83,89,97,101,103,107,109,113,127,131,137,139,149]
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

for i in range(1, 100000):
    t = getTriangleNumber(i)
    f = primeFactorization(t)
    if f  > 500:
        print t
        break
    
print "done"
    
    
    