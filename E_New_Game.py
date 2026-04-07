import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    vals = []
    cnts = []
    
    i = 0
    while i < n:
        j = i
        while j < n and arr[j] == arr[i]:
            j += 1
        vals.append(arr[i])
        cnts.append(j - i)
        i = j
    
    left = 0
    curr_sum = 0
    ans = 0
    
    for right in range(len(vals)):
        curr_sum += cnts[right]
        
        if right > 0 and vals[right] != vals[right - 1] + 1:
            left = right
            curr_sum = cnts[right]
        
        while right - left + 1 > k:
            curr_sum -= cnts[left]
            left += 1
        
        if curr_sum > ans:
            ans = curr_sum
    
    print(ans)