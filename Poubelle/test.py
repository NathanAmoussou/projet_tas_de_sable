from random import *

size = 3
l = [[0]*size for i in range(size)]
for row in l:
    print(' '.join(str(x) for x in row))

print()

l = [[0]*size for i in range(size)]
for x in range(size):
    for y in range(size):
        l[x][y] = randint(1, 3)

for row in l:
    print(' '.join(str(x) for x in row))


val = []
rn = []
cn = []
row = []

"""for rownum, row in enumerate(l):
    rn.append(rownum)
    for colnum, value in enumerate(l):
        val.append(value)
        cn.append(colnum)"""


lesvaleurs = []
leslignes = []
lescolonnes = []
for x, y in enumerate(l):
    for j, z in enumerate(y):
        leslignes.append(x) 
        lescolonnes.append(j)
        lesvaleurs.append(z)

print(leslignes)
print(lesvaleurs)
print(lescolonnes)

"""print(val)
print(rn)
print(cn)"""
