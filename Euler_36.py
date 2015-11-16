'''

Euler Problem

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_palindrome(num):
    num = str(num)
    if num[:1] == num [-1:]:
        if len(num) in [2,3]:
            return True
        return is_palindrome(num[1:-1])
    else:
        return False

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])

psum = 1
for j in range(2,10):
        bi =  toBinary(j)
        bi = str.lstrip(bi,'0')
        if is_palindrome(bi):
            psum += j

for i in range(10,1000000):
    if is_palindrome(i):
        bi =  toBinary(i)
        bi = str.lstrip(bi,'0')
        if is_palindrome(bi):
            psum += i

print psum
