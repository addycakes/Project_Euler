'''
Euler Problem 68

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a"magic" 5-gon ring?

'''

import itertools

nums = [1,2,3,4,5,6,7,8,9,10]
maxTotal = 0
combinations = itertools.permutations(nums, 10)

for comb in combinations:
    a=comb[0]
    b=comb[1]
    c=comb[2]
    d=comb[3]
    e=comb[4]
    f=comb[5]
    g=comb[6]
    h=comb[7]
    i=comb[8]
    j=comb[9]

    if a > d or a > f or a > h or a > j:continue
        
    ring1 = a+b+c
    ring2 = d+c+e
    ring3 = f+e+g
    ring4 = h+g+i
    ring5 = j+i+b

    if ring1 != ring2 or ring1 != ring3 or ring1 != ring4 or ring1 != ring5:continue

    pattern = [a,b,c,d,c,e,f,e,g,h,g,i,j,i,b]
    total = int(''.join(str(x) for x in pattern))

    if len(str(total)) > 16:continue
    
    if total > maxTotal:
        maxTotal = total
        mComb = comb
        
print maxTotal
