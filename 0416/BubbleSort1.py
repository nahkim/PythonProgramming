#bubble sort

#a = [5,4,3,2,1]

def bubbleSort(a):
    m = len(a) - 1 
    while m > 0:
        i = 0
        j = 1
        while j <= m:
            if a[i] > a [j]:
                a[i],a[j] = a[j],a[i]
            i += 1
            j += 1
        m -=1
    return a    #print(a)

a = [5,4,3,2,1]
print(bubbleSort(a))

#리스트는 0 부터 시작하니까 a 길이를 -1 해줘야 함
