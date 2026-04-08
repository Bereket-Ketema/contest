import sys

input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [1] + list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        a.sort()
        b.sort()
        
        def check(k):
            for i in range(k):
                if a[i] >= b[n - k + i]:
                    return False
            return True
            
        low, high = 0, n
        max_k = 0
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                max_k = mid     
                low = mid + 1     
            else:
                high = mid - 1    
                
        print(n - max_k)

solve()