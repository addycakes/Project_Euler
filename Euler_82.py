'''
Euler Problem 82

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only
moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only
moving right and down.

260324
'''
import urllib2
response = urllib2.urlopen('https://projecteuler.net/project/resources/p082_matrix.txt')
html = response.read()
rows = html.split("\n")

for row in rows:
    if len(row) < 79:
        rows.remove(row)
        continue
    new_row = row.split(',')
    for item in new_row:
        try:
            new_row[new_row.index(item)] = int(item)
        except ValueError:
            print item
    rows[rows.index(row)] = new_row

grid = [0,0]*40
for i in range(80):
    grid[i] = rows[i][79]

for j in range(79):
    x = 78 - j
    grid[0] += rows[0][x]
    for k in range(1,80):
        if grid[k-1]+rows[k][x] < grid[k] + rows[k][x]:
            grid[k] = grid[k-1]+rows[k][x]
        else:
            grid[k] = grid[k] + rows[k][x]

    for m in range(79):
        y = 78 - m
        if grid[y] < grid[y+1] + rows[y][x]:
            grid[y] = grid[y]
        else:
            grid[y] = grid[y+1] + rows[y][x]

print min(grid)

