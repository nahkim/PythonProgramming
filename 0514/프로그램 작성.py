# 영문 소문자로 이루어진 문자열을 입력 받아 암호문으로 변환하는 프로그램 작성
        
def encipher(p,k):
    n = len(p)
    c = ''
    i = 0
    while i < n:
        a = ord(p[i])
        if a == 32:
            a = 96
        t = a + k
        if t > 122:
            t = t - 27
        if t == 96:
            t = 32
        c = c + chr(t)
        i += 1      #위치 주의!!

    return c

A = input('평문 입력 : ')
K = int(input('K 값 입력(1~26) : '))
print('암호문:',encipher(A,K))
