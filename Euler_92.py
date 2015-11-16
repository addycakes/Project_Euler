'''
Euler Problem 92

A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

'''


def recursiveSquareChain(start):
    string = str(start)
    square_sum = 0
    for digit in string:
        square_sum += int(digit) ** 2

    if square_sum == 1:
        return False
    elif square_sum == 89:
        return True
    else:
        return recursiveSquareChain(square_sum)

endsIn89 = 0

for i in range(1,10000001):
    if recursiveSquareChain(i):
        endsIn89 += 1

print endsIn89
