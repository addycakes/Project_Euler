﻿'''

Euler Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value for SKY
is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?

'''

import urllib2
response = urllib2.urlopen('http://projecteuler.net/project/resources/p042_words.txt')
html = response.read().replace('"','')
words =  html.split(",")

triangleNums = []
for i in range(1,1001):
    triangleNums +=[ int( ((.5) * i * (i+1)) ) ]      

alphabet = [a for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def isTriangleWord(word):
    wordSum = 0
    for letter in word:
        wordSum += alphabet.index(letter)+1

    if wordSum in triangleNums:
        return True
    else:
        return False

tWords = 0    
for word in words:
    if isTriangleWord(word):
        tWords += 1

print tWords
