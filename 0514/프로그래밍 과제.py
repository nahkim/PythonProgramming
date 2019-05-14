# 암호화된 문자열을 복호화하여 다시 평문으로 변환하는 함수 decipher(c)를 작성
# encipher(p,k)/decipher(c,k)

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
        i += 1

    return c

def decipher(c,k):
    n = len(c)
    q = ''
    i = 0
    while i < n:
        a = ord(c[i])
        if a == 32:
            a = 123
        t = a - k
        if t < 96:
            t = t + 27
        if t == 96:
            t = 32
        q = q + chr(t)
        i += 1

    return q

A = input('평문 입력 : ')
K = int(input('K 값 입력(1~26) : '))
print('암호문 :',encipher(A,K))
print('복호화된 평문 :',decipher(encipher(A,K),K))
