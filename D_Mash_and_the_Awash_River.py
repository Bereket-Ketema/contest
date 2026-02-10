from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    

    if "**" in s or "*<" in s or ">*" in s or "><" in s:
        print(-1)
    else:
        c = Counter(s)
        l = c["<"]
        r = c[">"]
        m = max(l,r) + c["*"]
        print(m)