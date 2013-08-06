import math
'''
    a+b+c = 1000
    a**2 + b**2 = c**2
    a**2 + b**2 == (1000 - a - b)**2'''

for x in range(1, 1000):
    for y in range(1, 1000):
        if (x**2 + y**2) == ((1000-x-y)**2):
            c = x**2 + y**2
            c = math.sqrt(c)
            print(x*y*c)
