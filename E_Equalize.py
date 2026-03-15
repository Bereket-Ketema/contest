t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    left = 0
    ans = 1
    
    for right in range(n):
        while a[right] - a[left] > right - left:
            left += 1
        ans = max(ans, right - left + 1)
    
    print(ans)