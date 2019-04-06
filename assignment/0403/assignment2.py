#과제2 줄바꿈

N = int(input('N = '))

i = 1
a = 1
while i <= N:    
    if i == a: 
        print(i,end='\n')
        a = (a*2)+1
        
    else:
        print(i , end=' ')
    i += 1

