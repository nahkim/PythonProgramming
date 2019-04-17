#중복된 문자열제거
def delDup(x):
    n= len(x)
    s= ''
    for i in range(len(x)):     
         if s.count(x[i])==0:
            s += x[i]
    return s

s=input('s =')

print('중복이 제거된 문자열:',delDup(s))
