t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    ans = float('inf')
    for x in range(35):
        new_b = b + x

        if new_b == 1:
            continue
        temp = a
        ops = x

        while temp > 0:
            temp //= new_b
            ops += 1

        ans = min(ans, ops)

    print(ans)