'''
Euler Problem 15

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

#prepare grid with boundary set
grid = {}
for i in range(21):
    for j in range(21):
        grid[(i,j)] = 0

        if i  == 20:
            grid[(i,j)] = 1

        if j == 20:
            grid[(i,j)] = 1


grid[(20,20)] = 0

for i in range(1,21):
    for j in range(1,21):
        x = 20-i
        y = 20-j

        grid[(x,y)] = grid[(x+1,y)] + grid[(x,y+1)]

print grid[(0,0)]

        


'''
failed algorithms

remaining = True
routes = {}
while remaining:
    route = [0]
    pos = route[-1]
    for i in range(41):
        if i in route:
            continue
        else:
            if i == pos * h or i == pos * h +1:
                try:
                    if i not in routes[pos]:
                        routes[pos] += [i]
                        remaining = True
                    else:
                        remaining = False

                except KeyError:
                    routes[pos] = [i]
            
        
print 2**21
#tree has for binaryTree[node] = (left child, right child)
binaryTree = {}

vertices = 0
for i in range(0,21):
    vertices += i + 1

print 2* vertices

print len([(i,j) for i in range(21) for j in range(21)])

root = (0,0)

vertices = [(i,j) for i in range(21) for j in range(21)]

combinations = itertools.permutations(vertices,40)

valid = 0
for comb in combinations:
    sorted(comb)
    x = 0
    y = 0
    isValid = True
    for vertice in comb:
        if (vertice[0] == x or vertice[0] == x+1) and (vertice[1] ==y or vertice[1] == y+1) :
            x = vertice[0]
            y = vertice[1]
            isValid = True
        else:
            isValid = False
            break
    if isValid:
        valid += 1

print valid
    


i=0
routes = {}
while i != 21:
    for 
    
'''
