a = int(input('- 입력 : '))

while a < 2:
    print('2보다 큰 자연수 입력')
    a = int(input('- 입력 : '))
for k in range(2,a+1):
    s = 0
    for i in range(1, int(k/2)+1):
        if k % i == 0:
            s += i
    if s == k:
        print(k, end=' ')
