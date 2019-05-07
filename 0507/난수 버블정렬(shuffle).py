#난수를 발생시켜 버블정렬(shuffle)

def bubble(a,n):

    
    while n-1 > 0:
        i = 0    
        while i < n-1:
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            i += 1
        n -= 1

    return a

import random #, time
N = int(input('N = '))
a=list(range(1,N+1))
random.shuffle(a)
print(a)
#start = time.time()
b = bubble(a, N)
#end = time.time() - start
print(b)
#print(end)

