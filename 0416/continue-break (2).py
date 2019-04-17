#에라토스테네스의 체

#import time
N = int(input('N = '))
a = list(range(N+1))
a[1] = 0

#start = time.time()

for i in range(2, int(N/2)+1):
    for j in range(i, int(N/2)+1):
        if i*j <= N and a[i*j] == 0:   #핵심:이조건이 충족되면 아래문장이 실행안됨
            continue
        if i*j <= N:
            a[i*j] = 0
        else:
            break               #for 문으로 넘어감
for i in range(N+1):
    if a[i]:
        print(a[i], end=' ')

#end = time.time() - start
#print('\n',end)
