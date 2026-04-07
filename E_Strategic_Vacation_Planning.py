import sys
from bisect import bisect_right
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    
    vouchers = []
    groups = defaultdict(list)
    
    for _ in range(n):
        l, r, cost = map(int, input().split())
        dur = r - l + 1
        vouchers.append((l, r, cost, dur))
        groups[dur].append((l, r, cost))
        
    start_times = {}
    suffix_mins = {}
    
    for dur in groups:
        groups[dur].sort(key=lambda v: v[0])
        st = [v[0] for v in groups[dur]]
        start_times[dur] = st
        
        sm = [0] * len(st)
        sm[-1] = groups[dur][-1][2]
        for i in range(len(st)-2, -1, -1):
            sm[i] = min(sm[i+1], groups[dur][i][2])
        suffix_mins[dur] = sm
        
    ans = float('inf')
    
    for l, r, cost, dur in vouchers:
        rem = x - dur
        
        if rem in groups:
            st = start_times[rem]
            pos = bisect_right(st, r)
            
            if pos < len(st):
                ans = min(ans, cost + suffix_mins[rem][pos])
                
    print(ans if ans != float('inf') else -1)

solve()