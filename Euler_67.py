'''

Euler Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
'''

import urllib2
response = urllib2.urlopen('https://projecteuler.net/project/resources/p067_triangle.txt')

triangle = {}

k = 0
for line in response.readlines():
    line = line.replace('\n','')
    triangle[k] = [int(x) for x in line.split(' ')]
    k += 1

for i in range(99):
    row = triangle[99-i]
    row2 = triangle[99-i-1]
    for j in range(len(row2)):
        element = row2[j]
        left = row[j]
        right = row[j+1]

        if left > right:
            row2[j] =  element + left
        else:
            row2[j] =  element + right

print triangle[0][0]
        
