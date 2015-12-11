'''
Euler Problem 81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only
moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only
moving right and down.
'''
import urllib2
response = urllib2.urlopen('https://projecteuler.net/project/resources/p081_matrix.txt')
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

for k in range(1,80):
    rows[79][79-k] += rows[79][79-k+1]
    rows[79-k][79] += rows[79-k+1][79]

for i in range(1,80):
    for j in range(1,80):
        if rows[79-i+1][79-j] > rows[79-i][79-j+1]:
            rows[79-i][79-j] += rows[79-i][79-j+1]
        else:
            rows[79-i][79-j] += rows[79-i+1][79-j]

print rows[0][0]
