#매개변수로 주어진 m이 완전수인지 판별하는 함수  isPerfect(m)을 사용하여, 2부터 N까지의 자연수 중에서 완전수를 출력하는 프로그램 작성

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
            
