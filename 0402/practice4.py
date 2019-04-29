#매개변수로 주어진 m과 n의 최소공배수를 반환하는 함수 lcm(m, n)을 사용하여 자연수 a와 b의 최소공배수를 구하는 프로그램 작성

def lcm(m,n):
    M = m
    N = n
    while M != N:
        if M > N:
            N = N+n
        else:
            M = M+m
    return M


a = int(input('a = '))
b = int(input('b = '))
print('최소공배수 : ',lcm(a,b))
