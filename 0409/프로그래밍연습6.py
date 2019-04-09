def sum_avg(x,y,z):
    global s
    global v
    s = x+y+z
    v = s/3

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
sum_avg(a,b,c)
print('합 :',s)
print('평균 :',v)
