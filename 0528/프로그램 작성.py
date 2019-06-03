#텍스트와 패턴을 입력하여
#텍스트에서 패턴이 처음 발견된 위치를 출력하는 프로그램 작성

def stringSearch(t,p,i):
    j = 0
    N = len(t)
    M = len(p)
    while i < N and j < M:
        if t[i] != p[j]:
            i -= j
            j = -1
            i += 1
            j += 1
        if j == M:
            return i - M
        else:
            return i
        
f = open('input.txt', 'r')
text = f.read()
print('텍스트 : ', text)
f.close()
pattern = input('패턴 입력 : ')
i = 0
N = len(text)
M = len(pattern)
while M > 0:
    l = stringSearch(text,pattern,i)
    i = l + M
    if i < N:
        print('패턴을 발견한 위치 :',l)
    else:
        break
print('문자열 탐색 완료.')
