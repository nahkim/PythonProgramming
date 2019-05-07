#어구 전철인지 여부를 판별

def isAnagram(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()   #주의!!
    list2.sort()

    #print(a1, a2)

    i = 0
    while n2 > i:
        if list1[i] != list2[i]:
            return False
        i += 1
    return True

S1 = input('S1 = ')
S2 = input('S2 = ')

if isAnagram(S1,S2):
    print('어구 전철')
else:
    print('어구 전철이 아님')


