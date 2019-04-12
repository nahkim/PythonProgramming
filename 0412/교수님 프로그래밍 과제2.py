#과제 2 소수 갯수와 프로그램의 실행시간(비효율적)


import time
N = int(input('2 이상의 자연수 입력 :'))
a = list(range(N+1))
a[1] = 0
i = 2
start = time.time()
while i <= N/2:
    j = 2
    while i*j <= N:
        a[i*j] = 0
        j += 1
    i += 1
end = time.time() - start
count = 0

for k in range(N+1):
    if a[k]: count += 1
print('실행시간:',end)
print(count,'개의 소수 발견')
