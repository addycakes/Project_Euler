'''
Euler Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n > 1?

'''

def isPandigital(num):
    
    num = str(num)
    r = range(1,len(num)+1)
    for digit in num:
        if int(digit) not in r:
            return False
        r.remove(int(digit))
    
    return True

def concatProduct(n,l):
    product = ''
    for m in l:
        product += str(m*n)

    return int(product)

maxP = 0
for i in range(1,10000):
    s= []
    for j in range(1,10000):
        s+= [j]
        p = concatProduct(i,s)
        if len(str(p)) == 9:
            if isPandigital(p):
                if p > maxP:
                    maxP = p
        elif len(str(p)) > 9:
            break

print maxP
