#주사위를 N번 던졌을 때 각 면이 나오는 확률을 계산하는 프로그램 작성

def castDice(N):
    a = []
    for i in range(N):
        a.append(random.randint(1,6))
    #print(a)

    return a



import random
N = int(input('N = '))
A = castDice(N)

print(A)
i=1
while i <= 6:
    print(i,'   ', A.count(i)/N*100,'%')
    i += 1


