'''
Euler problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

num = 2**1000
digit_sum = 0
for i in str(num):
    digit_sum += int(i)

print digit_sum
