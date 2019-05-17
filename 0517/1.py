#1

def makeMatrix(n):
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            if i == j:
                b.append(0)
            b.append(random.randint(0,2))
        a.append(b)
    return a


def printMatrix(a):
    n = len(a)
    s = -n
    for i in range(n):
        for j in range(n):
            print(a[i][j],end= ' ')
            if a[i][j] == a[j][i]:
                s += 1
        print()

    return int(s/2)


import random

n = int(input('n ='))
b = makeMatrix(n)
print('대칭인 원소의 개수 :',printMatrix(b))
