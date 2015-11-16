'''
Euler Problem 17

If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

NumbersToWords = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
                  8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",
                  15:"fifteen", 16:"sixteen", 17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
                  30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
                  100:"hundred",1000:"thousand"};

def countLetters(word):
    count = 0
    for l in word:
        count += 1

    return count

def reduceNum(num):
    #print "number: " + str(num)
    words = []
    isFinished = False
    
    #get ones, tens, and hundreds (i.e. 234 -> 234, 34, 4)
    onesNum = num % 10
    tensNum = num % 100
    hundredNum = num % 1000

    #number not above 100
    if tensNum == num:
        isFinished = True
        #print "true " + str(tensNum)
        
    try:
        words += [NumbersToWords[tensNum]]
        hundredNum -= tensNum
        #print NumbersToWords[tensNum]
    except KeyError:

        if onesNum != 0:
            words += [NumbersToWords[onesNum]]
        #print "ones: " + str(onesNum)

        tensNum -= onesNum
        if tensNum != 0:
            words += [NumbersToWords[tensNum]]
        #print "tens: " + str(tensNum)

        hundredNum -= (tensNum + onesNum)

    if not isFinished:
        #print "hundreds: " + str(hundredNum)
        if hundredNum != 0:
            h  = hundredNum / 100
            words += [NumbersToWords[h]]
            words += NumbersToWords[100]
            if tensNum != 0 or onesNum != 0:
                words += ["and"]                

    numberForWord = 0
    for word in words:
        numberForWord += countLetters(word)
    return numberForWord

total_letters = 0
for i in range(1,1001):
    word = ""

    #these two dictionary items need a number qualifier
    if i == 100 or i == 1000:
        total_letters += countLetters("one")
    try:
        word =  NumbersToWords[i]
    except KeyError:
        word = ""
        
    if word is not "":
        total_letters += countLetters(word)
    else:
        total_letters += reduceNum(i)

print total_letters
