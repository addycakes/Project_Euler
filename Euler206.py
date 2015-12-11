'''
Euler Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

'''

import re

def checkNum(n):
    number = str(n)
    m = re.match(r'1.2.3.4.5.6.7.8.9.0', number, re.M)

    if m: print number

for i in range(1000000000,1400000000):
    checkNum(i**2)
