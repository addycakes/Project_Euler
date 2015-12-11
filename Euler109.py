'''
Euler Problem 109

In the game of darts a player throws three darts at a target board which is split
into twenty equal sized sections numbered one to twenty.


The score of a dart is determined by the number of the region that the dart lands in.
A dart landing outside the red/green outer ring scores zero.
The black and cream regions inside this ring represent single scores.
However, the red/green outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region, or bulls-eye.
The outer bull is worth 25 points and the inner bull is a double, worth 50 points.

There are many variations of rules but in the most popular game the players will begin
with a score 301 or 501 and the first player to reduce their running total to zero is a winner.
However, it is normal to play a "doubles out" system, which means that the player must
land a double (including the double bulls-eye at the centre of the board) on their final dart to win;
any other dart that would reduce their running total to one or lower means the score for that
set of three darts is "bust".

When a player is able to finish on their current score it is called a "checkout" and the
highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

D3	
D1	D2	 
S2	D2	 
D2	D1	 
S4	D1	 
S1	S1	D2
S1	T1	D1
S1	S3	D1
D1	D1	D1
D1	S2	D1
S2	S2	D1

Note that D1 D2 is considered different to D2 D1 as they finish on different doubles.
However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for example,
D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?
38182
'''

#dartValues
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25]
d = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,50]
t = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60]

pairValues = {'sd' : [(x+y) for x in s for y in d],
              'st' : [(x+y) for x in s for y in t],
              'dt' : [(x+y) for x in d for y in t]}
ss = []
for i in range(len(s)):
    for j in range(i,len(s)):
        ss += [s[i] + s[j]]
        
dd = []
for i in range(len(d)):
    for j in range(i,len(d)):
        dd += [d[i] + d[j]]
        
tt = []
for i in range(len(t)):
    for j in range(i,len(t)):
        tt += [t[i] + t[j]]

pairValues['ss'] = ss
pairValues['dd'] = dd
pairValues['tt'] = tt

n = 0
remainder = []
for score in range(2,100):
    for num in d:
        v = score - num
        if v == 0:
            n += 1
        elif v > 0:
            remainder += [v]
        elif num > v:
            break

for r in remainder:
    for key in pairValues:
        for value in pairValues[key]:
            if r - value == 0:
                n += 1
    for x in s:
        if r - x == 0:
            n += 1
    for y in d:
        if r - y == 0:
            n += 1
    for z in t:
        if r - z == 0:
            n += 1

print n

