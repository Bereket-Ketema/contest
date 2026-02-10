from collections import Counter
n = int(input())

for _ in range(n):
    s = input()
    t = input()
    p = input()

    sc = Counter(s)
    tc =  Counter(t)
    pc = Counter(p)
    ptr1 , ptr2 = 0 , 0

    while ptr1 < len(s) and ptr2 < len(t):
        if s[ptr1] != t[ptr2]:
            ptr2 += 1
        else:
            ptr1 +=1
            ptr2 +=1
    if ptr1 == len(s):
        f = True
        for k in tc:
            if tc[k] > sc[k] + pc[k]:
                f = False
                break
        if f:        
            print("YES")
        else:
            print("NO")
    else:
        print("NO")