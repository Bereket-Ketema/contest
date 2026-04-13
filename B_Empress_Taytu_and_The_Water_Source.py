def can(s, d, a, k):
    total_time = 0
    for i in range(len(d)):
        trips = (d[i] + s - 1) // s
        total_time += trips * a[i]

        if total_time > k:
            return False
    return True


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    low, high = 1, max(d)
    answer = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if can(mid, d, a, k):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)