#에라토스테네스의 체

def erathos(a, n):
    a[1] = 0
    i = 2

    while i <= n/2:
        j = 2
        while i * j <= N:
            a[i*j] = 0
            j += 1
        i += 1
    return a


N = int(input('N= '))
a = list(range(N+1))
b = erathos(a, N)
print(b)
