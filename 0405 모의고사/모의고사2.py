#화씨를 섭씨로 변경

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    a,b=b,a
while a <= b:
    F = a*9/5+32
    print('섭씨 :',a,'화씨 :',F)
    a = a+5
