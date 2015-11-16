'''
Euler Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value
of the denominator.
'''
from fractions import Fraction

def cancelDigits(numer,denom):
    numer = str(numer)
    denom = str(denom)

    if int(denom) % 10 == 0 and int(numer) % 10 == 0:
        return 1000
    
    canCancel = False
    for digit in numer:
        if digit in denom:
            denom = str.replace(denom,digit,'',1)
            numer = str.replace(numer,digit,'',1)
            canCancel = True
            break

    if not canCancel:
        return 1000
    elif int(denom) == 0:
        return 1000
    else:
        return (int(numer)*1.0)/int(denom)

nonTrivials = []
for i in range(10,100):
    for j in range(10,100):
        d = (1.0*i)/j
        if d >= 1:
            continue
        else:
            cd = cancelDigits(i,j)
            if cd >= 1:
                continue
            elif d == cd:
                nonTrivials += [(i,j)]

pD = 1
pN = 1
for n in nonTrivials:
    pN *= n[0]
    pD *= n[1]

print Fraction(pN,pD)

