#지역변수 c (전달이 안됨 add 함수 내에서만 사용가능)
def add(a,b):
    c = a + b

a =int(input('정수 입력:'))
b =int(input('정수 입력:'))
c = 0
add(a,b)
print('c =',c)
