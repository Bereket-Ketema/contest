from sys import stdin


def ii():return int(stdin.readline().strip())
def ll():return list(map(int, stdin.readline().strip().split()))
def ss():return stdin.readline().strip()


def solve():
    n , m , v = ll()
    arr = ll()
    prefix = [0] * (n+1)
    sufix = [0] * (n+1)
    prefixsum = [0] * (n+1)


    for i in range(n):
        prefixsum[i] += arr[i] + prefixsum[i-1]

    tmp = 0
    for i in range(n):
        tmp += arr[i]
        if tmp >= v:
            prefix[i] = 1
            tmp = 0

        prefix[i] += prefix[i-1]

    tmp = 0
    suffixmap = {0:n}
    for i in range(n-1,-1,-1):
        tmp += arr[i]
        if tmp >= v:
            sufix[i] = 1
            tmp = 0

        sufix[i] += sufix[i+1]
        if sufix[i] not in suffixmap:
            suffixmap[sufix[i]] = i


    ans = -1
    for i in range(n):
        required = m-prefix[i-1] 
        j = -1
        if required in suffixmap:
            j = suffixmap[required]

        if i <= j:
            ans = max(ans , prefixsum[j-1] - prefixsum[i-1])


    print(ans)
    
tt = ii()
res = []
for _ in range(tt):
    solve()