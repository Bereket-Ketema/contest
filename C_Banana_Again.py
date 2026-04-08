n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
ans = float('inf')

def backtrack(i, curr):
    global ans
    if i == n:
        other = total - curr
        ans = min(ans, abs(curr - other))
        return
    
    backtrack(i + 1, curr + nums[i])
    
    backtrack(i + 1, curr)

backtrack(0, 0)
print(ans)