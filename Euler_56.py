'''
Euler Problem 56

A googol (10**100) is a massive number: one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
'''

def sumDigits(n):
    s = str(n)
    NumSum = 0

    for d in s:
        NumSum += int(d)

    return NumSum

digital_sums = []
for i in range(101):
    for j in range(101):
        digital_sums += [sumDigits(i**j)]

print max(digital_sums)
