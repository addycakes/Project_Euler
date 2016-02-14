'''
Euler Problem 98
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively,
we form a square number: 1296 = 362. What is remarkable is that, by using the same
digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call
CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not
permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, find all the square anagram word pairs
(a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

import urllib2
import math

response = urllib2.urlopen('https://projecteuler.net/project/resources/p098_words.txt')
html = response.read()
words = html.split(',')

squares = []
for s in  range(2,20000):
    squares += [s**2]

anagrams = {}
for w in words[2:]:
    l = []
    w = w[1:-1]
    l.extend(w)
    l.sort()
    ls = ''.join(l)
    if ls in anagrams:
        anagrams[ls] += [w]
    else:
        anagrams[ls] = [w]

def checkPairs(pair):
    p1 = pair[0]
    p2 = pair[1]

    tests = []
    for sqs in squares:
        if len(str(sqs)) == len(p1):
            tests += [sqs]

    maxSQ = 0
    for sq in tests:
        m = {}
        for i in range(len(p1)):
            char = p1[i]
            m[char] = str(sq)[i]

        num = ''
        for c in p2:
            if m[c] not in num:
                num += m[c]
            else:
                break

        if len(num) != len(p1):continue
        if num[0]=='0':continue
        if int(num) in squares:
            if sq > num:
                if sq > maxSQ:
                    maxSQ = sq
            else:
                if num > maxSQ:
                    maxSQ = num

    return int(maxSQ)


sorted_anagrams = anagrams.keys()
sorted_anagrams.sort(key = lambda s: len(s),reverse=True)

solutions = []
for a in sorted_anagrams:
    if len(anagrams[a]) == 2:
         solutions += [checkPairs(anagrams[a])]

print max(solutions)


