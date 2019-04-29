#매개변수로 주어진 m과 n의 최대공약수를 반환하는 함수 gcd(m, n)을 사용하여 자연수 a와 b의 최대공약수를 구하는 프로그램 작성

#호제법 이용

def gcd(m,n):
    while m % n != 0:
        m,n = n,m%n
        
    return n

a = int(input('a = '))
b = int(input('b = '))
print('최대공약수 : ', gcd(a,b))
