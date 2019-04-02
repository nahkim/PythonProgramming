#최소공배수

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
