'''
Euler Problem 99

Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing
one thousand lines with a base/exponent pair on each line, determine which line number
has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import math
import urllib2

response = urllib2.urlopen('https://projecteuler.net/project/resources/p099_base_exp.txt')
html = response.read()
lines = html.split("\n")

lineWithMax = 0
maxLog = 0
for line in lines:
    base,exp = line.split(',')
    log =  math.log(int(base)) * int(exp)

    if log > maxLog:
        maxLog = log
        lineWithMax = line

print lineWithMax
print lines.index(lineWithMax)+1
