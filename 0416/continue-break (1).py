#break 와 continue1
a = list(range(1,11))
print(a)
for i in a:
    if i == 8:
        break
    if i % 2 == 0:  #1 이면 짝수가 출력
        continue
    print(i, end=' ')
print()
print(i)
