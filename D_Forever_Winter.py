t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1

    cnt_deg1 = 0
    cnt_big = 0

    for i in range(1, n + 1):
        if deg[i] == 1:
            cnt_deg1 += 1
        else:
            cnt_big += 1

    x = cnt_big - 1
    y = cnt_deg1 // x

    print(x, y)