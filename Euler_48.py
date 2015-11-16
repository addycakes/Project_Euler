'''
Euler Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

'''

number = 0

for i in range(1,1001):
    number += i**i

string = str(number)

print string[-10:]
