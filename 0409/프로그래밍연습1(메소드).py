#count()와 append() 메소드를 사용하여 리스트의 데이터를 중복 없이 입력하는 프로그램 작성


a = int(input('정수 입력(종료시는 999):'))
b = []

while a != 999:
    if b.count(a) == 0 :
        b.append(a)
    a = int(input('정수 입력(종료시는 999):'))
print(b)
    
    
