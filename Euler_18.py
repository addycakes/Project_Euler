'''
Euler Problem 18


By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

'''
triangle = {0:[75],
            1:[95,64],
            2:[17,47,82],
            3:[18,35,87,10],
            4:[20,04,82,47,65],
            5:[19,01,23,75,03,34],
            6:[88,02,77,73,07,63,67],
            7:[99,65,04,28,06,16,70,92],
            8:[41,41,26,56,83,40,80,70,33],
            9:[41,48,72,33,47,32,37,16,94,29],
            10:[53,71,44,65,25,43,91,52,97,51,14],
            11:[70,11,33,28,77,73,17,78,39,68,17,57],
            12:[91,71,52,38,17,14,91,43,58,50,27,29,48],
            13:[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
            14:[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]}



for i in range(14):
    row = triangle[14-i]
    row2 = triangle[14-i-1]
    for j in range(len(row2)):
        element = row2[j]
        left = row[j]
        right = row[j+1]

        if left > right:
            row2[j] =  element + left
        else:
            row2[j] =  element + right

print triangle[0][0]
        

        
'''

failed algorithms

def sumTriangle(row, tri):
    left = 0
    right = 0

    for i in range(row+1,len(tri)):
        for j in range(len(tri[i])-1):
            left += tri[i][j]
            right += tri[i][j+1]
    if left > right:
        newTriangle = tri
        for element in newTriangle:
            row = newTriangle[element]
            row.pop(-1)
    else:
        newTriangle = tri
        for element in newTriangle:
            row = newTriangle[element]
            row.pop(0)

    return newTriangle

pos = 0
tsum = 0
for i in range(15):
    row = triangle[i]
    tsum += row[pos]

    triangle = sumTriangle(i,triangle)
    triangle.pop(i)

print tsum


for i in range(15):
    rsum = 0
    for k in triangle:
        row = triangle[k]
        try:
            rsum += row[i]
        except IndexError:
            continue
    print rsum

pos = 0
for k in triangle:
    row = triangle[k]
    m = max(row)
    print row.index(m)
    #print m
    
max_path = [0,0,1,2,2,3,3,3,4 ,5,6,6,6,6,7]

msum = 0
for i in range(15):
    msum += triangle[i+1][max_path[i]]

print msum


    
pos = 0
tsum = 0
positions = {}

for k in triangle:
    row = triangle[k]
    element = row[pos]
    try:
        positions[k] += [pos]
    except KeyError:
        positions[k] = [pos]
    
    tsum += element

    nextRowUsedPos = positions[k+1]
    nextPos = pos + 1


def findPath(start, triangle):
    pathTotal = triangle[15][start]
    print pathTotal
    
    pos = start
    for i in range(1,16):
        curRow = triangle[16 - i]
        nextRow = 16 - i - 1
        if nextRow == 0:
            return pathTotal #+ 75
        nextRow = triangle[16 - i - 1]
        
        curValue = curRow[pos]
        rightVal = 0
        leftVal = 0
        if pos < len(nextRow):
            rightVal = nextRow[pos]
        if pos-1 >=  0:
            leftVal = nextRow[pos-1]

        print str(leftVal )+ " " + str(rightVal)    
        if leftVal > rightVal:
            pathTotal += leftVal
            pos -= 1
            print leftVal
        else:
            pathTotal += rightVal
            print rightVal

for i in range(0,len(triangle[15])):
    print findPath(i,triangle)
    print "\n"
'''
