#완전수,과잉수,부족수

def isPerfect(x):
    i = 1
    s = 0

    while i <= x/2:
        if x % i == 0:
            s += i
        i += 1
    if s == x:
        return 1
    if s > x:
        return 2
    else:
        return 3


a = int(input('a = '))
b = int(input('b = '))

for i in range(a,b+1):
    if isPerfect(i) == 1:
        print(i,': 완전수')
    elif isPerfect(i) == 2:
        print(i,': 과잉수')
    else:
        print(i,': 부족수')
            
