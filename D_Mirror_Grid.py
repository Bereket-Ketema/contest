import sys

input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1
    
    # Read grid (each row is a string of 0/1 without spaces)
    grid = []
    for i in range(n):
        row = data[idx]
        idx += 1
        grid.append([int(c) for c in row])
    
    visited = [[False] * n for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            
            # Collect all unique positions in this 90° rotation orbit
            positions = []
            x, y = i, j
            seen = set()
            
            for _ in range(4):
                pos = (x, y)
                if pos not in seen:
                    seen.add(pos)
                    positions.append(pos)
                # Rotate 90° clockwise: (x,y) -> (y, n-1-x)
                nx = y
                ny = n - 1 - x
                x, y = nx, ny
            
            # Mark all positions in orbit as visited
            for px, py in positions:
                visited[px][py] = True
            
            # Get current values in this orbit
            values = [grid[px][py] for px, py in positions]
            
            count_1 = sum(values)
            count_0 = len(values) - count_1
            
            # Minimum flips for this orbit: choose the majority value
            answer += min(count_0, count_1)
    
    print(answer)