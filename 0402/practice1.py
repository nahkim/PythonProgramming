#3개 숫자 중 최대값 구하는 함수 max3(x,y,z)

def max3(x,y,z):
    if x > y:
        x,y = y,x
    if y > z:
        y,z = z,y
    
    return z

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
maxval = max3(a,b,c)
print('최대값 : ',maxval)
