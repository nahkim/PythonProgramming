#x의 y제곱을 구하는 함수 a,b

def power(x,y):
    res = x
    for i in range(y-1):
        res *=x
    return res

a = int(input('a = '))
b = int(input('b = '))
result = power(a,b)
print('결과 : ',result)
