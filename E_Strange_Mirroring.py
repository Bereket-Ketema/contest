t = int(input())

def find_char(level, pos, idx, s):
    if level == 1:
        return s[idx]

    half = 1 << (level - 2)

    if pos > half:
        return find_char(level - 1, pos - half, idx, s).swapcase()
    else:
        return find_char(level - 1, pos, idx, s)


for _ in range(t):
    s = input().strip()
    q = int(input())
    queries = list(map(int, input().split()))

    n = len(s)
    ans = []

    for k in queries:
        k -= 1
        block = k // n + 1
        idx = k % n
        ans.append(find_char(61, block, idx, s))

    print(*ans)