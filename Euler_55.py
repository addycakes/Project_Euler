'''
Euler Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through
the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers,
and for the purpose of this problem, we shall assume that a number is
Lychrel until proven otherwise. In addition you are given that for every number below
ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one,
with all the computing power that exists, has managed so far to map it to a palindrome. In fact,
10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

'''

def is_palindrome(num):

    num = str(num)
    if num[:1] == num [-1:]:
        if len(num) in [2,3]:
            return True
        return is_palindrome(num[1:-1])
    else:
        return False

def reverseNum(num):
    string = str(num)
    newNum = ''
    for i in range(1,len(string)+1):
        newNum = newNum + string[len(string)-i]

    return int(newNum)

def isLychrelNumber(num):
    tempLychrel = num
    for i in range(50):
        obverse = tempLychrel
        reverse = reverseNum(tempLychrel)
        lSum = obverse + reverse
        if is_palindrome(lSum):
            return False
        else:
            tempLychrel = lSum
            
    return True

Lychrel_Numbers = []

for i in range(10, 10001):
    if isLychrelNumber(i):
        Lychrel_Numbers += [i]

print len(Lychrel_Numbers)
        