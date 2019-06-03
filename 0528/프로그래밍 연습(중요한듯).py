#프로그래밍 연습 남꺼

def makeList(x):
    a = []
    i = 0
    while i < len(x):
        b = ''
        while i < len(x) and x[i].isalpha():
            b += x[i]
            i += 1
        i += 1
        if b != '':
            a.append(b)
    return a

fin = open('input.txt')
line = fin.read()
A = makeList(line)
print(A)
fin.close()
