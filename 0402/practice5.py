#완전수

def isPerfect(m):
    i = 1
    k = 0
    while i <= m/2:
        if m % i == 0:
            k += i
        i += 1

    if k == m:
        return True
    else:
        return False

N = int(input('N = '))
for i in range(1, N+1):
    if isPerfect(i):
        print(i,end=' ')
            
