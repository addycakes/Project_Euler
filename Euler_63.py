'''
Euler Problem 63

The 5-digit number, 16807=7**5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

'''
import math

solutions = 0
n = 1
x = 0

while (x < 10):
    x = math.ceil(10 ** ((n-1.0)/n))
    solutions += 10 - x
    n += 1

print solutions
