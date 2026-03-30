import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
k = int(data[index])
index += 1
h = [int(data[i]) for i in range(index, index + n)]

max_a = 0
left = 0
max_d = deque()
min_d = deque()

for right in range(n):
    while max_d and h[max_d[-1]] <= h[right]:
        max_d.pop()
    max_d.append(right)
    
    while min_d and h[min_d[-1]] >= h[right]:
        min_d.pop()
    min_d.append(right)
    
    while h[max_d[0]] - h[min_d[0]] > k and left <= right:
        left += 1
        while max_d and max_d[0] < left:
            max_d.popleft()
        while min_d and min_d[0] < left:
            min_d.popleft()
    
    max_a = max(max_a, right - left + 1)

L = max_a
pairs = []
if L > 0:
    max_d = deque()
    min_d = deque()
    for i in range(n):
        while max_d and max_d[0] < i - L + 1:
            max_d.popleft()
        while min_d and min_d[0] < i - L + 1:
            min_d.popleft()
        
        while max_d and h[max_d[-1]] <= h[i]:
            max_d.pop()
        max_d.append(i)
        
        while min_d and h[min_d[-1]] >= h[i]:
            min_d.pop()
        min_d.append(i)
        
        if i >= L - 1:
            cur_max = h[max_d[0]]
            cur_min = h[min_d[0]]
            if cur_max - cur_min <= k:
                start = i - L + 1
                end = i
                pairs.append((start, end))

print(max_a, len(pairs))
for start, end in pairs:
    print(start + 1, end + 1)