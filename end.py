"""
#줄바꿈을 하지 않고 모든 데이터를 한 줄에 나오게 하기

for i in range(1,11): print(i, end=' ')

#띄어쓰기 대신 콤마를 넣고 싶은 경우

for i in range(1,11): print(i, end=',')
"""
#마지막 콤마를 출력하지 않는 경우
for i in range(1,11):
    if i < 10: print(i, end=',')
    else: print(i,end='')
