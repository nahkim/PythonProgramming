# 숫자로 된 문자열 2개를 입력 받은 다음, 문자열을 자연수로 바꾸어 주는 프로그램 작성

def makeNum(x):
    s = 0
    for i in range(len(x)):
        s *= 10
        s += ord(x[i]) - 48     #a = ord(x[i]) - 48
        #s = s + a * 10^i 왜 이건 안됨?
                                #s += a
    return s

a = input('a = ')
b = input('b = ')
A = makeNum(a)
B = makeNum(b)
C = A + B
print(C)
