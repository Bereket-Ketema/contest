import math
import sys

input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        low, high = 1, 2000000000000000000
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            on_bulbs = mid - math.isqrt(mid)
            
            if on_bulbs >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        print(ans)

solve()