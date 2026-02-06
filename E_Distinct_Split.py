from collections import Counter
t = int(input())



for _ in range(t):
    
    l = int(input())
    s = input()
    ans = 0
    le = set()
    r = Counter(s)
    for ch in s:
        
        le.add(ch)
        r[ch] -= 1
        if r[ch] == 0:
            del r[ch]

        ans = max(ans, len(le) + len(r))

        
    
    print(ans)