'''
Euler Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and
66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of
its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''
import math

def permutationsInSet(n, numbers):
    permutations = [n]
    for num in numbers:
        if num != n:
            if isPermutation(n,num):
                permutations += [num]

    return permutations
    
def isPermutation(num,num2):
    string = str(num)
    string2 = str(num2)

    if len(string) != len(string2):
        return False
    
    for digit in string2:
        if digit not in string:
            return False
        else:
            string = str.replace(string,digit,'',1)

    return True

cubes = []
for i in range(2, 10000):
    cubes += [i**3]

for cube in cubes:
    perms = permutationsInSet(cube, cubes)
    if len(perms) == 5:
        print perms

