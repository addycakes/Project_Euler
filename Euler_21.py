'''
Euler Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def getFactors(n):
    half = n / 2
    factors = []
    for i in range(1,half+1):
        if n % i == 0:
            factors += [i]

    return factors

def sumList(l):
    NumSum = 0

    for n in l:
        NumSum += n

    return NumSum

FactorsDict = {}

for i in range(1, 10000):
    l = getFactors(i)
    FactorsDict[i] = sumList(l)

amicable_pairs = []
for key in FactorsDict:
    factorSum = FactorsDict[key]
    if factorSum == key:
        continue
    try:
        if FactorsDict[factorSum] == key:
            if factorSum not in amicable_pairs:
                amicable_pairs += [factorSum]
            if key not in amicable_pairs:
                amicable_pairs += [key]
    except KeyError:
        failed = ""

            
print sumList(amicable_pairs)
