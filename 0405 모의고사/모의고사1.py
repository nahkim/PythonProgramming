N = int(input('N = '))

while N < 3:
    print('3이상 자연수 입력')
i = 1
a = 1
b = 1
c = 0
print(a,b,end=' ')
while i <= N-2:
    c = a+b
    print(c,end=' ')
    i += 1
    a = b
    b = c
