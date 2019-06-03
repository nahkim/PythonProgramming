#텍스트에 패턴이 여러 개 있을 경우
#패턴을 발견한 위치를 모두 찾아서 출력해 주는 프로그램 작성

def stringSearch(t,p):
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    while i < N and j < M:
        if t[i] != p[j]:
            i = i- j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    return i


fin = open('input.txt')
a = fin.read()
fin.close()

print('텍스트 :',a)
b = input('패턴 입력:')
print('패턴을 처음 발견한 위치:',stringSearch(a,b))
