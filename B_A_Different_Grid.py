t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = [list(map(int, input().split())) for _ in range(n)]
    
    if n * m <= 2:
        print(-1)
        continue
    
    if m > 1:
        for i in range(n):
            row = a[i]
            print(*(row[1:] + row[:1]))
    else:
        for i in range(n):
            print(a[(i + 1) % n][0])