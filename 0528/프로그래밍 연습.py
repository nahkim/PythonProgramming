#프로그래밍 연습 다시

def makeList(x):
    a = []
    fin = open(x)
    text = fin.read()
    b = len(text)
    
    for i in range(b):
        while text.isalpha(i):
            s += i
        if i == ord(32):
            a.append(s)

print(makeList('input.txt'))
