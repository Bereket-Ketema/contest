import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

def count_1543_in_border(border_str):
    s = border_str + border_str[:3]  
    cnt = 0
    for i in range(len(border_str)):
        if s[i:i+4] == '1543':
            cnt += 1
    return cnt


for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    grid = []
    for i in range(n):
        row = data[index]
        index += 1
        grid.append(list(row))  # list of chars '0'..'9'
    
    total = 0
    layer = 0
    
    while layer * 2 < n and layer * 2 < m:
        top = layer
        bottom = n - 1 - layer
        left = layer
        right = m - 1 - layer
        
        
        if top > bottom or left > right:
            break
        
       
        border = []
        
       
        for c in range(left, right + 1):
            border.append(grid[top][c])
        
        
        for r in range(top + 1, bottom + 1):
            border.append(grid[r][right])
        
       
        for c in range(right - 1, left - 1, -1):
            border.append(grid[bottom][c])
        
       
        for r in range(bottom - 1, top, -1):
            border.append(grid[r][left])
        
        
        border_str = ''.join(border)
        
        
        total += count_1543_in_border(border_str)
        
        layer += 1
    
    print(total)