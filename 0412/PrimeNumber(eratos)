#프로그램 작성(1) 에라토스테네스의 체 방법으로 소수 출력

N = int(input('자연수 N 입력 :'))
a = list(range(N+1))
a[1] = 0
i = 2
while i <= N/2:
    j = 2
    while i*j <= N:
        a[i*j] = 0
        j += 1
    i += 1
for k in range(N+1):  
    if a[k]:
        print(a[k], end =' ')
