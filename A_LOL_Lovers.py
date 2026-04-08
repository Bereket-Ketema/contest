n=int(input())
s=input()
for i in range(1,n):
    s1 = s[:i]
    s2 = s[i:]
    if s1.count('L') != s2.count("L") and s1.count('O') != s2.count('O'):
        print(i)
        break
else:
    print(-1)