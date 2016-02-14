'''
Euler Problem 89
For a number written in Roman numerals to be considered valid
there are basic rules which must be followed. Even though the rules allow some numbers
to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to
be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers
written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the
definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive
identical units.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.

Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.

'''

import urllib2
response = urllib2.urlopen('https://projecteuler.net/project/resources/p089_roman.txt')
RNS = response.readlines()

def findSubtractivePair(numeral):
    
    pairs = [ ('DCCCC','CM'), ('CCCC','CD'),('LXXXX','XC'),('XXXX','XL'),('VIIII','IX'),('IIII','IV')]

    for pair in pairs:
        if pair[0] in numeral:
            numeral = numeral.replace(pair[0],pair[1])
            
    return numeral

chars1 = 0
chars2 = 0
for RN in RNS:
    chars1 += len(RN)
    RN = findSubtractivePair(RN)
    chars2 += len(RN)

print chars1-chars2
