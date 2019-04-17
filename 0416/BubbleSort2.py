#bubble sort

def bubblesort(a):
    n = len(a)-1
    while n > 0:
        i = 0
        j = 1
        while j<=n:
            if a[i] > a[j]:
                a[i], a[j] = a[j],a[i]

            i += 1
            j += 1
        n -= 1
        print(a)
    return a

N = int(input('N = '))
A = list(range(N, 0, -1))
#A = [5,4,3,2,1]
print(A)
bubblesort(A)
