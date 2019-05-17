#2

def winner(a,b):
    if a == '가위':
        if b == '보':
            return 1
        elif b == '바위':
            return 2
        else:
            return 3

    elif a == '바위':
        if b == '가위':
            return 1
        elif b == '보':
             return 2
        else:
            return 3

    elif a == '보':
        if b == '바위':
            return 1
        elif b == '가위':
            return 2
        else:
            return 3
    

import random
c = ['가위','바위','보']
b = random.choice(c)
print('A 선택')
a = input('A : ')
#print(a)
#print(a != '가위')
while a != '가위' and a !='바위' and a !='보':
    print('가위, 바위, 보만 입력하세요.')
    a = input('A : ')
 
'''print('B 선택')
b = input('B : ')
while b != '가위' or '바위' or '보':
    print('가위, 바위, 보만 입력하세요.')
print(winner(a,b))'''

if winner(a,b):
    if winner(a,b) == 1:
        print('A 승')
    elif winner(a,b) == 2:
        print('B 승')
    else:
        print('무승부')
