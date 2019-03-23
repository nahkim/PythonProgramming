#자연수 N을 입력 받은 다음, 1부터 N까지 자연수의 합을 계산하여 출력하는 프로그램 작성
"""
#while 문
N = int(input('N = '))
i = 1
s = 0
while i <= N:
    s += i
    i += 1
print('합: ',s)
"""
#for 문
N = int(input('N = '))
s = 0
for i in range(1,N+1):
    s += i
print('합: ',s)
