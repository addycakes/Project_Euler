'''

Euler Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

string = ''

for i in range(1,1000001):
    string += str(i)

digits = [1,10,100,1000,10000,100000,1000000]

product = 1
for digit in digits:
    product *= int(string[digit-1])
    
print product
