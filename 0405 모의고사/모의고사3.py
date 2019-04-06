#isPrime(x)사용

def isPrime(x):
    a = 2
    while a <= x/2:
        if x % a == 0:
            return False
        a += 1
    return True

N = int(input('N = '))

for i in range(2,N+1):
    if isPrime(i):
        print(i,end=' ')
