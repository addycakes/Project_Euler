'''
Euler Problem 31

In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''
combinations = 0

i = 200
while i >= 0:
    j = i
    while j >= 0:
        k = j
        while k >= 0:
            l = k
            while l >= 0:
                m = l
                while m >= 0:
                    n= m
                    while n >= 0:
                        o = n
                        while o >= 0:
                            combinations += 1
                            o -= 2
                        n -= 5
                    m -= 10
                l -= 20
            k -= 50
        j -= 100
    i -= 200

print combinations
