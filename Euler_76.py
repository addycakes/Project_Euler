'''
Euler Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''

combinations = [0]*101
combinations[0] = 1

for i in range(1,100):
    for j in range(i,101):
        combinations[j] += combinations[j-i]
print combinations[-1]
