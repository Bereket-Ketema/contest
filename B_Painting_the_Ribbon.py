import math

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    mx = math.ceil(n / m)
    if n - mx > k:
        print("YES")
    else:
        print("NO")