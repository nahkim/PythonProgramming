#m이 n 의 약수인지 여부를 판별하는 함수isDivisor(m,n)

def isDivisor(m,n):
    if m % n == 0:
        return True
    else:
        return False
        

a = int(input('a = '))
for i in range(1,a+1):
    if isDivisor(a,i):
        print(i, end=' ')   #a의 모든 약수
