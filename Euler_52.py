'''

Euler Problem 52

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

def isPermutation(l):
    for num in l:
        string = str(num)
        for num2 in l:
            string2 = str(num2)
            for digit in string2:
                if digit not in string:
                    return False
    return True

for i in range(1,1000000):
    b = 2 * i
    c = 3 * i
    d = 4 * i
    e = 5 * i
    f = 6 * i

    if isPermutation([b,c]):
        if isPermutation([d,e]):
            if isPermutation([e,f]):
                if isPermutation([d,c]):
                    print i
                    
