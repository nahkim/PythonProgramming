#프로그램의 실행시간 측정(4)
#숫자 큰거 넣어야함(10만 정도)

import time
N = int(input('자연수 N 입력 : '))
s = 0
start = time.time()
for i in range(1, N*N+1):#N의 제곱에 비례
    s += i
end = time.time() - start
print('합계:',s)
print('실행시간:',end)

