#난수를 발생시켜 버블정렬(randint)

def bubble(a,n):

    
    while n-1 > 0:
        i = 0    
        while i < n-1:
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            i += 1
        n -= 1

    return a

import random
N = int(input('N = '))
a=[]
for i in range(N):
    a.append(random.randint(1,N))
print(a)
b = bubble(a, N)
print(b)
