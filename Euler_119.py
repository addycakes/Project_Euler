'''
Euler Problem 119
Published on Friday, 7th April 2006, 06:00 pm; Solved by 8086; Difficulty rating: 30%
The number 512 is interesting because it is equal to the sum of its digits raised
to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this
property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must
contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

nums = []
for b in range(2,100):
    for a in range(2,10):
        e = pow(b,a)
        if sum(map(int,str(e)))==b:
            nums += [e]

n = sorted(nums)
print n[1]
print n[9]
print n[29]
