def isOdd(num):
    if num % 2 ==1:return True
    else: return False

N = int(input('자연수 N 입력 : '))
for i in range(1,N+1):
    if isOdd(i):print(i,end=' ')
