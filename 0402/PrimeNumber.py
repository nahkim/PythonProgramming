# a까지의 소수출력

a = int(input('- 입력 : '))

while a < 2:
    print('2보다 큰 자연수 입력')
    a = int(input('- 입력 : '))
    
for k in range(2,a+1):
    s = 0
    isPrime = True
    for i in range(2, int(k/2)+1):
        if k % i == 0:
            isPrime = False

    if isPrime:
        print(k, end = ' ')
