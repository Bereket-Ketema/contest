t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    score = 0
    for i in range(n):
        if i % 2 == 0:
            score += a[i]
        else:
            score -= a[i]
    
    remain = k
    for i in range(1, n, 2):
        if remain == 0:
            break
        can = a[i-1] - a[i]
        if can > 0:
            add = min(can, remain)
            score -= add
            remain -= add
    
    print(score)