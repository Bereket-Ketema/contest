from sys import stdin


def ii():return int(stdin.readline().strip())
def ll():return list(map(int, stdin.readline().strip().split()))
def ss():return stdin.readline().strip()


def solve():
    n = ii()
    arr = ll()
    prefix = [0] * (n + 2)
    ans = 0
    for i in range(n):
        if arr[i] < i + 1:
            prefix[i] += 1

        prefix[i] += prefix[i - 1]

        if arr[i] < i + 1:
            ans += prefix[arr[i] - 2]

    print(ans)
    
tt = ii()
res = []
for _ in range(tt):
    solve()