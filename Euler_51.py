'''
Euler Problem 51

By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number
is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member
of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
'''

import math

template = ['XXBBBX','XBXBBX','BXBXBX','BBXXBX','BBBXXX','BXBBXX','BXXBBX','BBXBXX','XBBBXX','XBBXBX']

def is_prime(num):
    if num <= 0:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def putRepeatedDigitInPattern(digit,pattern):
    products = []
    for p in pattern:
        k = p.replace('B',str(digit))
        products += [k]

    return products

def putRegularDigitsInPattern(digits,pattern):
    products = []
    for p in pattern:
        k = p.replace('X',digits[0],1)
        k = k.replace('X',digits[1],1)
        k = k.replace('X',digits[2],1)
        products += [k]

    return products


def checkResults(terms):
    familySize = 0
    for term in terms:
        n = int(term)
        if len(str(n)) == 6:
            if is_prime(int(term)):
                familySize += 1

    if familySize == 8:
        return True
    else:
        return False

patterns = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
p9 = []
p10 = []

for i in range(10):
    results = putRepeatedDigitInPattern(i,template)
    p1 += [results[0]]
    p2 += [results[1]]
    p3 += [results[2]]
    p4 += [results[3]]
    p5 += [results[4]]
    p6 += [results[5]]
    p7 += [results[6]]
    p8 += [results[7]]
    p9 += [results[8]]
    p10 += [results[9]]

patterns = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

solutions = []
for i in range(100,1000):
    digits = str(i)
    for p in patterns:
        results = putRegularDigitsInPattern(digits,p)
        if checkResults(results):
            print results
            solutions += [results]
            break

