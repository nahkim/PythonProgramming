#호제법 이용

def gcd(m,n):
    while m % n != 0:
        m,n = n,m%n
        
    return n

a = int(input('a = '))
b = int(input('b = '))
print('최대공약수 : ', gcd(a,b))
