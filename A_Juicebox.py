import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    
    brand = [0] * (k + 1)
    
    for _ in range(k):
        line = input().split()
        b = int(line[0])
        c = int(line[1])
        brand[b] += c
    
    profits = []
    for i in range(1, k + 1):
        if brand[i]:
            profits.append(brand[i])
    
    profits.sort(reverse=True)
    
    ans = 0
    m = min(n, len(profits))
    for i in range(m):
        ans += profits[i]
    
    print(ans)