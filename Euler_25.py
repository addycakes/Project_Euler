'''
Euler Problem 25

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

f1= 1
f2 = 1
fN = 0
i = 2
while len(str(fN))<1000:
    i+= 1
    fN = f1 + f2
    f1 = f2
    f2 = fN

print fN
print i
