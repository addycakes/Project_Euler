import math

'''
Euler Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

#print pythagoreanSet(120)
'''

def pythagoreanSet(num):
    #return all (a,b,c) for right trianges with perimeter == num

    possible_triangles = 0
    for a in range(1, num):
        for b in range(1, a):
            if (a + b + math.sqrt( (a**2 + b**2) ) ) == num:
                possible_triangles += 1

    return possible_triangles

max_triangles = []
for i in range(0,1000):
    max_triangles += [(pythagoreanSet(i),i)]

print max(max_triangles)
