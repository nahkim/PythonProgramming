#순서대로 나오는 거
c = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]
for i in range(len(c)):
    print(len(c[i]))    #원소의 갯수 출력
    for j in range(len(c[i])):
        print(c[i][j], end=' ')
