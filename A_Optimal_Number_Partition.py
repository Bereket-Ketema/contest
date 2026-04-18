import math
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n // 2):
  ans += pow((arr[i] + arr[-(i + 1)]),2)
print(ans)