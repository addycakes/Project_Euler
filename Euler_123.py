'''
Euler Problem 123

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
(pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10.
'''

f = open("primes.txt", 'r')

x = 0
primes = []
for line in f:
    if x > 1:
        line.strip()
        l = line.split()
        primes += l
    x+=1

for n in range(7037, len(primes), 2):
    p = int(primes[n-1])
    r = 2 * p * n
    
    if r > 10**10:
        print n
        print r
        break
