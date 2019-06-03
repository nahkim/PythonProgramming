#텍스트와 패턴을 입력하여
#텍스트에서 패턴이 처음 발견된 위치를 출력하는 프로그램 작성
#다시..


def stringSearch(t,p):
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    q = 0
    while q <= N and q <= M:
        while i < N and j < M:
            if t[i] != p[j]:
                i = i- j
                j = -1
            i += 1
            j += 1
        if j == M:
            print('패턴을 처음 발견한 위치:',i - M)
        print('패턴을 처음 발견한 위치:',i)
        q += 1


fin = open('input.txt')
a = fin.read()
fin.close()


print('텍스트 :',a)
b = input('패턴 입력:')
stringSearch(a,b)
print('문자열 탐색 완료.')
