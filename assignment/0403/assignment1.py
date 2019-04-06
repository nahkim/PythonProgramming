#과제1 다항식을 구성하는 항의 값

a = int(input('a = '))
x = int(input('x = '))
e = int(input('e = '))

if e < 0 :
    print('e에 양의 정수를 입력하시오.')
    
elif e == 0:
    print('계산 결과 :',a)

else:
    i = 1
    s = x
    while e > i :
        s*x
    
        s = s*x
        i += 1

    print('계산 결과 :',a*s)
            
