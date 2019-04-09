#3차원 리스트 출력

d = [[[1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10]]]

for i in range(len(d)):
    for j in range(len(d)):
        for k in range(len(d[i][j])):            
            print(d[i][j][k], end=' ')
        print()
    print()


#print 함수를 어느블럭에 넣으면 바뀌는지 보기!!

    #프로그래밍을 주고 출력이 어떻게 되는지 써라 100퍼 셤
    #출력 값을 주고 프로그래밍 작성 100퍼 --이건 요번에 이런식으로 안나옴

'''
d = [[[1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10]]]

for i in range(len(d)):
    for j in range(len(d)):
        for k in range(len(d[i][j])):            
            print(d[i][j][k], end=' ')
        print()

'''
