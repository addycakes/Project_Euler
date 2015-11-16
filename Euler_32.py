'''
Project Euler 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1
through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it
once in your sum.
'''

def isPandigital(num):
    
    num = str(num)
    r = range(1,len(num)+1)
    for digit in num:
        if int(digit) not in r:
            return False
        r.remove(int(digit))
    
    return True

def concatMultisAndProduct(x,y,z):
    return str(x)+str(y)+str(z)

pandigital_sums = {}

for i in range(2,100000):
    for j in range(1,i):
        product = i * j
        pTest = concatMultisAndProduct(i,j,product)

        if len(pTest) > 9:
            break
        elif len(pTest) < 9:
            continue
        
        if isPandigital(pTest):
            pandigital_sums[product] = 1

psum = 0
for ps in pandigital_sums:
    psum += ps

print psum
