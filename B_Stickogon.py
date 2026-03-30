from collections import Counter
t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  freq = Counter(arr)
  count = 0
  for k in freq:
    if freq[k] >= 3:
      count += freq[k] // 3
  print(count)