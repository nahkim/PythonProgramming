
def inputPoly():
    print()

def printPoly(p):
    print()

def evalPoly(p,x):
    print()

def addPoly(a,b):
    print()

def multiplyPoly(a,b):
    print()

m = 1
P = []
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) : '))
    if m == 1:
        print('다항식 입력 선택\n')
        #P = inputPoly()
    elif m == 2:
        print('다항식 출력 선택\n')
        #P = inputPoly(P)
    elif m == 3:
        print('다항식 계산 선택\n')
        #P = inputPoly(P)
        #X = int(input('X = '))
        #result = evalPoly(P, X)
        #print('계산 결과 : ', result)
    elif m == 4:
        print('다항식 덧셈 선택\n')
        #A = inputPoly()
        #B = inputPoly()
        #printPoly(A)
        #printPoly(B)
        #C = addPoly(A, B)
        #printPoly(C)
    elif m == 5:
        print('다항식 곱셈 선택\n')
        #A = inputPoly()
        #B = inputPoly()
        #printPoly(A)
        #printPoly(B)
        #C = addPoly(A, B)
        #printPoly(C)
    else:
        if m != 9:
            print('메뉴 선택 오류\n')
