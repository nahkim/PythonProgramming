def isDivisor(m,n):
    if m % n == 0:
        return True
    else:
        return False
        

a = int(input('a = '))
for i in range(1,a+1):
    if isDivisor(a,i):
        print(i, end=' ')
