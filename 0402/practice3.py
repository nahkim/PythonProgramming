#매개변수로 주어진 m과 n의 최대공약수를 반환하는 함수 gcd(m, n)을 사용하여 자연수 a와 b의 최대공약수를 구하는 프로그램 작성


# i 사용

def gcd(m,n):
    i = 1

    while i <= m and i <= n:
        if m % i == 0 and n % i == 0:
            g = i
        i += 1
    return g

a = int(input('a = '))
b = int(input('b = '))
print('최대공약수: ', gcd(a,b))
